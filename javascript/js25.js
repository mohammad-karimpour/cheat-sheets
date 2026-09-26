// متد filter 
// جستجوی برا اساس یک شرط و برگرداندن داده ها
let nums = [1,2,3,4,5,65,67,89]

var fil = nums.filter((n)=>{
    return n > 5
})

console.log(fil);
// 65 67 89