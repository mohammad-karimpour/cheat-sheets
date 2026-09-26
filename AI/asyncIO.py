# asyncio = فانگشن منتظر و همزمانی و ناهمگام  با قابلیت صف بندی.
# IO bound : به پردازش های خارج از سرور و وابسته به سرور میزبان و پهنای باند. (درخواست API)
# CPU bound : پردازش هایی که در خود سیستم و سرور انجام میشوند. (حل مسئله داخلی)
# با این کتابخانه میتوان منتظر انجام کاری بمونیم. و در حالت پردازش آی او میتوان حالت همزمانی داشته باشیم.
# حالت همزمانی : کاری را که انجام آن زمان بر است و آی او باند است را تا دریافت پاسخ منتظر نمی مانیم. بلکه کار دیگری را کنارش انجام میدهیم.
# حالت صف بندی چیست؟ یعنی میتوانیم تسک هایی را ایجاد کنیم که به نوبت ولی همزمان انجام بشن.


#[--- CPU bound (5s) ---][----- IO bound (7s) -----] task 1
#........................[--CPU bound (5s)--][--- IO bound (6s) ---] task 2
#........................................... [-CPU bound (4s)-][-IO bound (5s)-] task 3
# no async => (5 + 7)(5 + 6)(4 + 5) = 32s
# asyncIO => (5 + 5 + 4 + 5) = 19s

import asyncIO


sem = asyncIO.Semaphore(3)

async def getnum(N):
    # منتظر ماندن
    async with sem:
        await asyncIO.sleep(1)
        await print(N)


async def main():
    tast_1 =  asyncIO.create_task(getnum(14))
    task_2 = asyncIO.create_task(getnum(0))

    tast_1
    task_2

    if 3<2:
        task_2.cancel()

    asyncIO.gather([
        getnum(5),
        getnum(15),
        getnum(25),
    ])        

    try:
       asyncIO.wait_for(tast_1, timeout=5)
    except:
       print('کار موفق نشد!')

    
    saf = asyncIO.Queue(maxsize=3)
    await saf.put('BMW') # 'گذاشتن | اگر پر باشد منتظر میماند تا جا باز شود
    car = await saf.get() # گرفتن | اگر خالی باشد منتظر یک آیتم میشود.
    saf.task_done() # اعلام پایان پردازش اون آیتم | بیشتر در کروتین ها استفاده میشود.
    saf.qsize() # اندازه فعلی صف
    saf.empty() # اگر صف خالی باشد
    saf.full() # اگر صف پر باشد
    await saf.join() # منتظر می‌مونه تا همه آیتم‌هایی که اضافه شدن، پردازش بشن

    try:
       saf.put_nowait('BENZ') # بدون انتظار یک آیتم را اضافه میکند.
    except asyncIO.QueueFull:
       print("صف پر است!")

    try:
       car_2 = saf.get_nowait() # بدون انتظار یک آیتم را بر میدارد.
    except asyncIO.QueueEmpty:
       print("صف خالی است!")  

asyncIO.run(main())





# coroutine (getnum()) = به تابعی که در آن عملیات غیر همزمان وجود دارد. 
# another coroutine(main()) = کروتین سطح بالا برای اجرای سایر کروتین های دیگر
# create_task = تسک ها برای انجام کار همزمان بکار میروند. تسک ها همه با هم اجرا میشوند.
# asyncio.gather = ایجاد لیستی از تسک ها برای اجرای همزمان
# asyncio.sleep = خوابیدن یا منتظر ماندن
# task_2.cancel = کنسل کردن تسک
# asyncio.wait_for = ایجاد محدودیت برای منتظر ماندن
# asyncio.Queue = صف | مانند جعبه ای که میتوان در آن چیزی گذاشت یا برداشت.
# برای ایجاد تعادل بین کاری که در آن تولید و پردازش است. اول ورود = اول خروج
# asyncio.Semaphore = در کروتین ها ایجاد میشود و محدودیت تعداد اجرای همزمان را بر عهده دارد.






async def worker(name, queue):
    while True:
        task = await queue.get()  # گرفتن کار از صف
        if task is None:
            break  # اگر تسک None بود، کار تمام شده است
        print(f"شروع {task} توسط {name}")
        await asyncIO.sleep(2)
        print(f"پایان {task} توسط {name}")
        queue.task_done()

async def main_2():
    queue = asyncIO.Queue()
    tasks = ['کار1', 'کار2', 'کار3']
    
    # تولیدکنندگان: قرار دادن وظایف در صف
    for task in tasks:
        await queue.put(task)

    # مصرف‌کنندگان: پردازش وظایف
    workers = [asyncIO.create_task(worker(f"کارگر{i + 1}", queue)) for i in range(3)]
    
    # منتظر ماندن تا تمام تسک‌ها پردازش شوند
    await queue.join()  # تا زمانی که همه وظایف پردازش شوند
    
    # ارسال علامت خاتمه به کارگران
    for worker_task in workers:
        await queue.put(None)  # ارسال None برای خاتمه دادن به کارگران
    
    # منتظر ماندن تا کارگران تمام شوند
    await asyncIO.gather(*workers)

asyncIO.run(main_2())