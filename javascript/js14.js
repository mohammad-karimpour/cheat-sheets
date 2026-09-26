//حلقه ها

/*
for (mabda;shart;code ezafi) {
    code
    
}*/


for(let num = 0; num < 10; num++){
     console.log(num);
}

// برای دیتا های قابل شمارش میتوان از حلقه for of استفاد کرد
// دیتا های قابل شمارش = آرایه و استرینگ و شبه آرایه ها

let name = 'mohammad'
for (s of name){
     console.log(s)
}
// برای دیتا های غیر قابل شمارش مانند آبجکت ها
let obj = {
     name:'mohammad',
     age:18
}

for (o in obj){
     console.log(o)
}