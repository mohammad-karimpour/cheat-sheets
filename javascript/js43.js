let h1 = document.querySelector('h1')

h1.style.cssText = 'color:red; font-size:12px;'

// برای دریافت مشخصات استایل یک تگ

consule.log(getComputedStyle(h1).color) // green