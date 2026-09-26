# صفات تابع

def num():
    pass

# برای استعلام صفات و متد های یک شی
dir(num)

# برای ایجاد یک صفت 
num.faeze = 'faezeamini'
setattr(num,'mohammad','mohammadkarimpour')


# گرفتن صفت های ساخته شده 
print(num.__dict__)
print(getattr(num,'faeze','gerl')) # سومین ورودی مقدار دیفالت است که درصورت نبود همچین صفتی خطا ندهد


# چک کردن وجود یک صفت در تابع
print(hasattr(num,'mohammad')) # True

# برای حذف یک صفت
del num.faeze
delattr(num,'mohammad')