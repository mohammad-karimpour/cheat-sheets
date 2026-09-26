// ست و مپ یک نوع داده هستند که مثل آرایه و آبجکت میباشند
// ست
let SET = new Set()

// برای اضافه کردن آیتم
SET.add(12)
// برای حذف آیتم
SET.delete(12)
// باری حذف کل آیتم ها
SET.clear()
// باری گرفتم اندازه ست
SET.size()
// برای جستجو یک آیتم
SET.has(12)

// ذخیره کردن یک آرایه به عنوان ست توی یک متغیر
let num = [1,2,3,4,5,6,7,8,9]
let NewSet = new Set(num)

// ذخیره کردن یک ست به عنوان آرایه توی یک متغیر
let NetArray = [...SET]



//مپ
//مپ مثل آبجکت است و کلید و ولیو دارد

let MAP = new Map()

// برای اضافه کردن آیتم
MAP.set('number', 12)
// برای حذف آیتم
MAP.delete('number')
// باری حذف کل آیتم ها
MAP.clear()
// باری گرفتم اندازه ست
MAP.size()
// برای جستجو یک آیتم
MAP.has('number')
// گرفتن یک آیتم
MAP.get('number')

// تبدیل کردن یک آبجکت به مپ
let NewMap = new MAP(Object.entries({'name': 'mohammad'}))
// تبدیل مپ به آبجکت
let NewObj = Object.fromEntries(MAP)


// پیشرفته : weekset,weekmap
// با این تفاوت که برای مقدار دهی حتما باید از آبجکت استفاده کرد و نمیتوان روی آن جستجو انجام داد
// برای پرفرمنس سیستم بهتره چون با حذف کردن این داده کلا پاک میشود و در استورج ردی باقی نمی زارد
let NewWeekSet = new WeakSet()
let NewWeekMap = new WeakMap()

// مقدار دهی
NewWeekSet.add({'1':'mohammad'})
NewWeekMap.set({'1':'name'},'mohammad')