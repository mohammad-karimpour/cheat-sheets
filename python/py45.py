"""تایپ دهی """
# این تایپ دهی در صورت سر پیچی ارور نمیدهد فقط توسط ادیتور یا پکیج مد نظر هشدار داده میشود
# پکیج مد نظر mypy است
# terminal => mypy  py45.py

from typing import *




""" تایپ ها """

string: str = 'mohammad'

number: int = 13

floats: float = 3.14

boolean: bool = True,False

const: final = 'const in js' # همان ثابت در جاوا اسکریپت است و غیر قابل مقدار دهی دوباره است

none: None = None # هیچ

types: str | int = 15  # دادن دو یا پند نوع تایپ به متغیر

optionalVar: Optional[str] = False  # تایپ آپشنال

types: Union[str,bool,int] = 1,False,'mm' # تعین چند نوع تایپ مجاز


lists: list[int] = [123,456] # داخل براکت نوع تایپ های مجاز را مینویسیم

dic: dict[str,int] = {'id':1 ,'name':45} # [KeyType , ValueType]

free: any = True,123 # هر تایپی مجاز است

items: Literal[True,False] = True # مقدار باید یکی از این مقادیر داخل براکت باشد






""" شی مجاز همان Enum در تایپ اسکریپت """

# شما میتوانید یک نوع نمونه برای تایپ دهی استفاده کنید
# بیشتر برای ورودی های بکار میرود که میگوییم ورودی حتما باید یک نوع از این کلاس - آبجکت - لیست و غیره باشد
class User:
    pass

U_1: User = 'nnn' # مقدار این متغیر باید از این کلاس - تابع و غیره باشد









""" اینترفیس """

# ساخت آبجکت با آیتم ها و تایپ های مشخص شده 

class Person(TypedDict):
    id: int
    name: str
    age : int
    live: bool

P_1: Person = {
    'id': 1,
    'name': 'mohammad',
    'age': 19,
    'live': True
}    





""" توابع """

def num(x:int , y:int , name:str) -> any: # تعین نوع خروجی یک تابع
    return f'{name} : {x+y}'




# از این دو کلمه میتوان استفاده کرد برای اینکه بگویم تابع خروجی ندارد

def ret(x:bool)-> NoReturn: # بهتر است
    print('mohammad', x)

def re()-> None:
    ret(True)    



# زمانی که ورودی فانکش یک فانکشن باشد
def callback(fun:callable):
    fun()



