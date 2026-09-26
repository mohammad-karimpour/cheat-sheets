let ul = document.createElement('ul')
ul.innerHTML = `<li>mohammad</li>`
ul.style.backgroundColor = 'red'

// نحوه append  کردن المنت ساخته شده
let div = document.querySelector('div')
div.append(ul)
div.appendChild(ul)

//نحوه پیشرفته اضافه کردن المنت ساخته شده
div.insertAdjacentHTML('afterend','<h4>hello</h4>')
/*
تمامی موقعیت ها

afterbegin => داخل تگ از اول
beforeend => داخل نگ از اخر

afterend => بعد از اتمام تگ اضافه بکن
beforebegin => قبل از شروع تگ اضافه بکن 

*/