// پرامیس = قول دادن
// برای کد هایی که تاخیر داند بکار میرود اگر توانست کار را انجام میدهد در غیر اینصورت یه کد دیگر را اجرا میکند

//پرامیس دو ورودی میگیرد که اولی برای اجرای موفق دومی برای اجرای ناموفق

let GetAPI = new Promise((resolve,reject)=>{
          let API = fetch('www.google.com')
          if(API.satusCode == 200){
            resolve('sucsess API')
          }else{
            reject('Error!')
          }
});

GetAPI.then(response => console.log(response)) // sucsess API  عملیات موفق
      .catch(response => console.log(response)) // Error!  عملیات نا موفق
      .finally(console.log('finish')) // finish  در هر صورت اجرا میشود


// شما میتوانید در then&... دستوراتی را بر روی خروجی اعمال کنید
// هر کدی را که در ان ریترن میکنید به عنوان ورودی به بعدی فرستاده میشود

let number = new Promise((resolve,reject)=>{
    resolve(1383)
    reject('Error')
})

number.then(num => { return num*2})
      .then(response => console.log(response)) // 2766
      .catch(ER => console.log(ER)) // Error