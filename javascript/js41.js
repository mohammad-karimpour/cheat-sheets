//برای ست کردن ایتم
localStorage.setItem('key','value');

//برای گرفتن 
localStorage.getItem('key')//=> value

//برای آبجکت ها

//باید برای ست کردن ان را به استرینگ تبدیل کرد
localStorage.setItem('key',JSON.stringify({key:'value'}))//=> string

//برای گرفتن باید ان را از حالت استرینگ خارج کرد
localStorage.getItem(JSON.parse('key'))//=> object
