 // callbackfunction  کالبک فانگشن
 //به تابعی که بعنوان ورودی به تابعی دیگر ارسال میشود میگویند

let pus = ()=>{
    return 1000
}

let num = (n)=>{
    console.log(n);
}

num(pus)