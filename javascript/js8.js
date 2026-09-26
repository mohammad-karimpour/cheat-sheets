//OR AND NOT

// OR => ||
// AND => &&
// NOT => !

/*
OR{
    true || true => true
    true || false => true
    false || true => true
    false || false => false
}
AND{
    true && true => true
    true && false => false
    false && true => false
    false && false => false
}
NOT{
    true => false
    false => true

}
*/
let num = !true // => false

if (12 == 23 || 12 < 23) {
    console.log(true);
}

if (12 == 23 && 12 < 23) {
    console.log(true);
}