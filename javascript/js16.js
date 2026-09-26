// array
//برای ذخیره کردن چند نوع و چند تعداد از دیتا

let ar = ['mohammad',12,true]
let arr = new Array('mohammad',false,56)

console.log(ar);
console.log(arr);

//برای ایجاد و مقدار دهی متغیر به ازای هر یک آیتم یک آرایه
let [name,age,life] = ar
console.log(name)// mohammad
console.log(age) // 12
//برای پرش روی یک آیتم
let [f1,,f3] = arr // f1 = mohammad , f3 = 56
// برای مقدار دهی دیفالت یک متغیر
let [name_2,age_2,life_2,color='red'] = arr
console.log(color)// red

// برای آبجکت ها
let user = {
    name_3:'sana',
    age_3:15,
    life:true
}
//در آبجکت ها باید حتما از خود اسم استفاده کرد و برای تغیر اسم باید از این روش استفاده کرد
let {name_3,age_3,life:zide,color_3='green'} = user
console.log(name_3 , age_3 , zide, color_3)// sana 15 true green

//از این روش میتوان خیلی راحت از آبجکت ها اطلاعات استخراج کرد
