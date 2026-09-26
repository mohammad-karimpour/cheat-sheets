// Class

class User{
    // پراپرتی هی کلاس
    constructor(id,name,family,age){ 
           this.id=id,
           this.name=name,
           this.family=family,
           this.age=age
    }
    // متد های کلاس
    FuulName(){
         return `user${this.id} : my name is ${this.name}${this.family} and ${this.age} year old`     
    }
}

// ساخت نمونه از کلاس
let mohammad = new User(1,'mohammad','karimpour',18);
let sana = new User(2,'sana','ghamisheh',15);
console.log(mohammad.name); // mohammad
console.log(sana.FuulName); // `user2 : my name is sanaghamisheh and 15 year old


// ارث برای
// ارث بردن از کلاسی دیگر به منزله عدم نوشتن کد تکراری

class User_2 extends User{
    constructor(name,family,job){
        super(name,family) //ارتباط با کلاس مد نظر
        this.job=job
    }
    Name(){
        console.log(this.name + this.family);
    }
}

let adel = new User_2('adel','mohammadzadeh','none');
console.log(adel.Name); // adel mohammadzadeh


//شما نمیتوانید مستقیم از ظریق کلاس به متدی دسترسی پیدا کنید باید حتما از طریق نمونه ساخته شده باشد 
// برای حل این مشکل میتوانید از متد های استتیک استفاده کنید
class User_3{
    constructor(name,family){
        this.family=family
        this.job=job
    }
static Name(){
        console.log(this.name + this.family);
    }
}

console.log(User_3.Name); // yes
console.log(User_2.Name); // Error