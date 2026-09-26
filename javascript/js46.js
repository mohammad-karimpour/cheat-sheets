// برای دریافت اطلاعات یک تگ میتوانیم از این روش استفاده کنیم

let butt = document.getElementById('#button')

butt.addEventListener('click', function(event){
    console.log(event); // کل مشخصات لاگ میشه
    if(event.key === 'Enter'){
        console.log('اینتر شد!');
    }
})