let Name = 'mohammad';
let family = 'karimpour';

//methods:
console.log(Name[2]);//=>h : با استفاده از ایندکس حرف را برمیگرداند

console.log(family.length);//=>9 : طول رشته را برمیگرداند

console.log(Name.concat(family));//=> mohammad karimpour

console.log('  m  '.trim());//=> اسپیس ها را پاک میکند

console.log('MOHAMMAD'.toLowerCase());//=> mohammad

console.log('mohammad'.toUpperCase());//=> MOHAMMAD

console.log(Name.search("mm"));//=> 4 از طریق ایندکس جایگاه آن را بهت میگوید 

console.log(family.includes('pour'));//=> true

console.log(Name.slice(4,8));//=> mmad برش استرینگ با ایندکس 

console.log(family.substring(1,5));//=> arim

console.log('mohammad-karimpour-18'.split('-'));//=> ['mohammad','karimpour','18']

console.log(eval('12 * 30'));//=> 360 محاسبات ریاضی که به صورت استرینگ نوشته شدن را حل میکند

console.log(Name.replace('m','s'));//=> sohammad تغیر یک عبارت 

// استرینگ پدینگ (عملیات روی اول و اخر استرینگ
// دو ورودی میگیرد(حد اکثر طول استرینگ و باقیمانده را چه پر کند

// از اول
console.log(Name.padStart(20,"*")) //************mohammad
// از آخر
console.log(Name.padEnd(20,"*")) //mohammad************
