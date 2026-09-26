""" Error handeling """

# هندل کردن ارور های کد

# try => کدی را مینویسی که میخواهیم هندلش کنیم اگر ارور داشت به اکسپت میرود و در غیر اینصورت کد اجرا میشود
# except => اگر کد با ارور مواجه شد کد های این اجرا میشوند
# else => اگر کد بدون ارور اجرا شد و موفقیت آمیز بود این اجرا میشود
# finally => در هر صورت اجرا میشود - بیشتر برای اتمینان از اجرای ارور هندلر و یا پاک سازی و غیره استفاده میشود

try:
  print(5 / 0)

except:
   print('Error...')

else:
   print('successful - NoError...')

finally:
   print('End...')






try:
   print(5 / 0)

# هندل کردن نوع خاصی از ارور
except ZeroDivisionError:
   print('No Type Zero')

# هندل کردن چند نوع خاص از ارور
except (ValueError , TypeError):
   print('Error')

# اسم مخفف برای دریافت آن
# Exception => سر دسته ارور ها و بیشترشان را پوشش میدهد
except Exception as Ex:
   print(f'Error :{Ex}')   

# اگر ریترنی در کد اصلی وجود داشته باشد این از کار می افتد
else:
   print(':)')

# اگر ریترنی در این بدنه وجود داشته باشد کل کد های دیگر ارور هندلر از کار می افتد
finally:
   print('tmam')   






# هندلر تو در تو
try:
  print(5 / 0)

except:
   try:
     print(9 / 0)
 
   except:
      print('Error...')