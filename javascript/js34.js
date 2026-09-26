let h1elim = document.querySelector('.h1')

//کلیک کردن
h1elim.addEventListener('click',()=>{
    console.log('mohammad');
})
// برای راست کلیک کردن
h1elim.addEventListener('contextmenu',()=>{
    console.log('mohammad');
})
//برای ارسال داده یک فرم
h1elim.addEventListener('submit',()=>{
    console.log('mohammad');
})
//کلیک های کیبرد
h1elim.addEventListener('keypress',()=>{
    console.log('mohammad');
})
//کلیک موقع بالا اوردن کلید
h1elim.addEventListener('keyup',()=>{
    console.log('mohammad');
})
//کلیک موقع پایین اوردن کلیک
h1elim.addEventListener('keydown',()=>{
    console.log('mohammad');
})
//برای فرم ها وقتی که بازش میکنید
h1elim.addEventListener('focus',()=>{
    console.log('mohammad');
})
//برای فرم ها وقتی بسته میشود
h1elim.addEventListener('blur',()=>{
    console.log('mohammad');
})
//دو بار کلیک کردن
h1elim.addEventListener('dblclick',()=>{
    console.log('mohammad');
})
//زمانی که کاربر یک گذینه را تغیر میدهد
h1elim.addEventListener('change',()=>{
    console.log('mohammad');
})
//موقع کپی کردن
h1elim.addEventListener('copy',()=>{
    console.log('mohammad');
})
//موقع کات کردن
h1elim.addEventListener('cut',()=>{
    console.log('mohammad');
})
// موقع پیست کردن
h1elim.addEventListener('paste',()=>{
    console.log('mohammad');
})
//موقع لود کامل صفحه
h1elim.addEventListener('load',()=>{
    console.log('mohammad');
})
//موقع آنلاین بودن
h1elim.addEventListener('online',()=>{
    console.log('mohammad');
})
//موقع آفلاین بودن
h1elim.addEventListener('offline',()=>{
    console.log('mohammad');
})
//هنگام حرکت موس
h1elim.addEventListener('mousemove',()=>{
    console.log('mohammad');
})
//زمانی که متنی انتخاب شده
h1elim.addEventListener('select',()=>{
    console.log('mohammad');
})
//زمانی که کاربر لمس خود را حرکت میدهد
h1elim.addEventListener('touchmove',()=>{
    console.log('mohammad');
})
// زمانی که کاربر لمس را رها میکند
h1elim.addEventListener('touchend',()=>{
    console.log('mohammad');
})
//زمانی که کاربر صفحه را لمس میکند
h1elim.addEventListener('touchstart',()=>{
    console.log('mohammad');
})
//موقع اسکرول کردن
h1elim.addEventListener('scroll',()=>{
    console.log('mohammad');
})


///////////////////////////////////////////

//برای به دست اوردن اطلاعات ایونت میتوانید از این روش استفاده کنید
h1elim.addEventListener('click',(event)=>{

    event.preventDefault()// aption for submit event and more...
    console.log(event);
})



//////////////////////////////////////////////////

//برای حذف کردن یک ایونت

h1elim.removeEventListener('click',()=>{
    console.log('removed');
})

//////////////////////////////////////////////////

//ایجاد کانفیگبرای رویداد

h1elim.addEventListener('click',()=>{/*دستورات*/},{/* کانفیگ ها*/})

h1elim.addEventListener('click',()=>{console.log(12)},{ once=true})

// کانفیگ ها 

once // فقط یک بار رویداد اجرا میشود
