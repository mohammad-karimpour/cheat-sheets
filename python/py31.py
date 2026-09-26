# ژنراتور ها
# مثل تابع ها هستند ولی شما میتوانید خروجی آن را سازماندهی کنید
# در ژنراتور ها میتوان از چندین خروجی استفاده کرد
# شما میتوانید با هر بار صدا زدن ژنراتور به خروجی دیگر برسید

def num():
    print('one') # 0 next
    yield 1      # 1 next
    print('two') # 1 next
    yield 2      # 2 next
    print('tree')# 2 next
    yield 3      # 3 next

number = num()





#  با هر بار نکست زدن روی ژنراتور تا خروجی بعدی اجرا میشود

print(number) # => one

print(next(number)) # one
                    # 1
                    # two

print(next(number)) # 2
                    # tree

print(next(number)) # 3                






# سه متد

number.close()   # متوقف کردن ژنراتور
number.throw('ttt')  #گذاشتن یک استثنا



# مقدار دهی خروجی و ذخیره در یک متغیر
# مقدار دیفالت آن نان است و هیچ ربطی به خروجی ژنراتور ندارد

def foo():
    print('...')
    n = yield 55
    yield 12
    print(n)

# حتما باید از نکست استفاده کرد تا به یلد برسد

print(next(foo())) #  ...  55
foo().send('mohammad')
print(next(foo())) # 12   mohammad
