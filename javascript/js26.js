//جشتجو در یک ارایه اگر وجود داشت مقدارش را برمیگرداند

let names = ['mohammad','karimpour','Elina']

var search = names.find((useer)=>{
      return useer === 'karimpour'
})

console.log(search);// karimpour