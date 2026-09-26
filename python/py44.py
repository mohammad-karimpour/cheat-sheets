""" str - rper """

# str => داده استرینگ به صورت ساده برای استفاده عمومی
# rper =>  داده با جزییات کاملتر مخصوص توسعه دهنده

print(str("mohammad")) # => mohammad
print(repr("mohammad")) # => "mohammad"


# در کلاس ها هر دو همان رپر هستند بخواترهمین موقع پرینت کردن یک کلاس آدرس و نوع آن را به جای محتوای آن برمیگرداند
# برای شخصی سازی متد ها در کلاس

class users:
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'rper'   

print(str(users)) # => str 
print(repr(users)) # => rper   