//متد های آرایه

let arr = ['mohammad','karimpour',18,15,true,false];
let too = [12,23,45,6]

console.log(arr[1]);//برگرداندن دیتا با استفاده از ایندکس

console.log(arr.push(45));// ایتم داخل پرانتز را به اخر ارایه اضافه میکند

console.log(arr.pop());//اخرین ایتم را حذف میکند

console.log(arr.shift('javascript'));// ایتم داخل پرانتز را به اول ارایه اضافه میکند

console.log(arr.unshift());//اولین ایتم را حذف میکند

console.log(arr.toString());//ارایه را به یک رشته واحد تبدیل میکند

console.log(arr.join());//ارایه را به یک رشته واحد تبدیل میکند و هر چیزی که در پرانتز گذاشته شود را بیت ایتم ها ایجاد میکند

console.log(arr.splice(3,'9000'));//یک ایتم را اضافه میکند |ورودی اول:محل قرار گیری ورودی دو:ایتم جدید

console.log(arr.concat(too));//برای متصل کردن دو ارایه به هم

console.log(arr.sort());//برای مرتب کردن ارایه بر اساس حروف

console.log(arr.reverse());//برعکس کردن ارایه

console.log(Array.isArray(arr));//true => اگر ارایه باشد تروو را برمی گرداند

console.log(too.indexOf(3));// 2

console.log(arr.slice(1,4));//18 15

