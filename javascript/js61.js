// async await
// منتظر ماندن تا اجرای کد مد نظر

async function Getnum(){
  await setTimeout(()=>{
    let number = 20
    },2000)
     console.log(`number is : ${number}`);
}

Getnum() // no async =out=> number is : undefined
Getnum() // async =out=> number is : 20
