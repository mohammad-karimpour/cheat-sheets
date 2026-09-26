// تکرار
// setInterval

let num = 0

setInterval(()=>{

    console.log(num++);
    
},1000)
//  1000ms = 1s


//برای متوقف کردن
let time = setInterval(()=>{
     if(num == 10){
         clearInterval(time)
     }

    console.log(num++);
    
},1000)

// تاخیر 
// تاخیر بعد لود صفحه

setTimeout(()=>{
 
    console.log('mohammad');

},1000)

//برای ایجاد ورودی 

setTimeout((num,num2)=>{
 
    console.log(num + num2);

},1000,14,40)//54