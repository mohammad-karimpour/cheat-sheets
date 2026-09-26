""" دیتا کلاس """

# ایجاد کلاس به صورت خلاصه و ساده


from dataclasses import dataclass

# باید حتما تایپ آنهارا مشخص کرد
# مقادیر دیفالت حتما باید درآخر قرار بگیرند
# به صورت دیفالت برای نمونه ها صفت ست میشود


@dataclass(frozen=True) # داده ها غیر قابل تغیر میشوند
class User:

    name:str
    family:str
    age:int = 19 # تعین مقدار دیفالت

    def __post_init__(self): # این متد بعد از ساخت نمونه اجرا میشود
        print(self)



# ساخت نمونه
P_1 = User('mohammad', 'karimpour',24)
print(P_1)        