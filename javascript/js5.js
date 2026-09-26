// سترینگ ها

let Name = "mohammad";
let family = "karimpour";

console.log(Name + family); // mohammad Karimpour
 
console.log(Name + "\n" + family); // mohammad
                                   // karimpour
                                   

console.log("mohammad\"karimpour\""); // mohammad "karimpour"

//الان بهتر است از بک تیک برای ساخت استرینگ استفاده کرد

let STR = `mohammad
karimpour${Name}` //mohammad
                  //karimpourmohammad
console.log(STR)