//نحوه دسترسی به اتریبیوت های یک tag
let tag = document.querySelector('#app')

//برای گرفتن
tag.getAttribute('name')

//برای ایجاد یا تغیر
tag.setAttribute('class','btn')

// برای حذف یک اتریبیوت
tag.removeAttribute('class')

//برای اینکه بفهمیم یک اتریبیوت وجود دارد یا نه
tag.hasAttribute('class')// true || false


/////////////////////////////////////
//دسترسی به استایل المنت ها

tag.style.color = 'green'