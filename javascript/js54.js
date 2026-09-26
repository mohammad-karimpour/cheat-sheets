// با استفاده از پراکسی میتوان بر روی هر اتفاقی که روی یک آبجکت رخ میدهد ناظر باشیم و مانوری انجام دهیم
let user = {
    id: 1,
    name: 'mohammad',
    family: 'karimpour',
    age: 18,
}
// برای پراکسی کردن یک آبجکت
let Puser = new Proxy(user,{})

// هندلر های زیادی وجود دارد که میتوان با استفاده از آن مانور را انجام داد
// مثلا میخواهیم روی گرفتن آِیتم از آبجکت مانور بدهیم و برنامه جوریه که اگر آیتم خواسته شده وجود نداشت خودش بیاد جایگزین بزارد
let Getuser = new Proxy(user,{
    get(target,receiver) {
        // اگر آیتم مد نظر وجود داشت که همان را برگردان در غیر این صورت مقدار داده شده را برگردان
        return target[receiver] ? target[receiver] : 'no item...'
    }
})

console.log(user.life) // undefinted
console.log(Getuser.life) // no item...

// بعضی از هندلر ها
/*
* get
* set
* apply
* construct
* getPrototypeOf
* setPrototypeOf
* isExtensible
* preventExtensions
* getOwnPropertyDescriptor
* */