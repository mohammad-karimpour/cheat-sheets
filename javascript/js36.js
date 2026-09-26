let num_1 = document.querySelector('#num1');
let num_2 = document.querySelector('#num2');
let num_3 = document.querySelector('#num3');
let num_4 = document.querySelector('#num4');
let num_5 = document.querySelector('#num5');
let num_6 = document.querySelector('#num6');
let num_7 = document.querySelector('#num7');
let num_8 = document.querySelector('#num8');


//برای دسترسی به والد یک المنت
num_2.parentNode
num_1.parentElement

//برای دسترسی یه المت های قبلی
num_4.previousElementSibling// => num_3 برای المنت ها
num_1.previousSibling

//برای دسترسی به المت های بعدی
num_3.nextElementSibling// => num_4 برای المنت ها
num_2.nextSibling

//برای تشخیص تعداد فرزند ها
num_1.childElementCount

//دسترسی به فرزند ها
num_6.children
num_4.childNodes


//برای اینکه بفهمیم که یک والد فرزند دارد یا نه
num_8.hasChildNodes // => true || false


// برای دسترسی به اولین و اخرین فرزند
num_2.firstChild
num_5.lastChild


