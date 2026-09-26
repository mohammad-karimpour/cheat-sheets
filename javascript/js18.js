// const object = {
//     key:value
// }

const objects = {
    name:'mohammad',
    family:'karimpour',
    age:18,
    live: true
}

//فراخوانی object

console.log(objects['family']);//karimpour

console.log(objects.name);// mohammad


// برای حذف کردن یک ایتم از ابجکت

delete objects.family

// آبجکت ها یک دیتا غیر قابل پیمایش هستند و برای قابل پیمایش شدنش باید
let onPaymayesh = Object.entries(objects)
console.log(onPaymayesh) // [ [ 'name', 'mohammad' ], [ 'age', 18 ], [ 'live', true ] ]


let one = 1
let two = 2
let three = 3

// اگر میخواهید مقداری را در آبجکت ذخیره کنید که از جایی دیگر می آید فقط لازم است آن را صدا کردن
let nums ={
    one,
    two,
    three
} 