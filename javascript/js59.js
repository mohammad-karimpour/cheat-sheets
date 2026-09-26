
// array.reduce( function(total, currentValue, currentIndex, arr), 
// initialValue )

let arr = [200, 25, 50, 25];

// خلاصه کردن یک ارایه
let out = arr.reduce((total,current)=>{
         (total,current)=> total - current

})

console.log(out); // 100  total=200 - current=25 =(175) nextcorse=> total=corrent=175 - current=50  =(125) nextcorse=> total=corrent=125 - current=25  =(100)


let out_2 = arr.reduce((total, currentValue, currentIndex, arr)=>{
    (total,current,currentIndex,arr)=>  [ total - current,currentIndex,arr]

})
// out =>
/*
1-[200,25,0,arr] = 175
1-[175,50,1,arr] = 125
1-[125,25,2,arr] = 100
*/