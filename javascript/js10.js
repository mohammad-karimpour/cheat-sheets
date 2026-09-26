// Switch Case
// برای اجرای شرط های اغلبا اعداد
let num = 2 + 2;

switch (num) {
  case 3:
    alert( 'Too small' );
    break;
  case 4://true
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too big' );
    break;
  default:
    alert( "I don't know such values" );
    break;
}

// case => if & else if
// default => else