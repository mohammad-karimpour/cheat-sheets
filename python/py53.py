""" دکوریتور ها در با کلاس """

# برای این کار حتما باید این دو متد را در کلاس ایجاد کنید
# __init__ => برای گرفتن متد مد نظر که رویش مانور بدهیم 
# __call__ =>  برای مانور زدن روی متد گرفته شده


class dec:
    def __init__(self,func) -> None:
        self.func = func

    def __call__(self):
        # قبل از خزوجی متد 
        print("$" *20)   
        self.func
        # بعد از خروجی متد
        print("$" *20)


 # استفاده هم برای تابع و هم برای کلاس

@dec
class User:
    pass

@dec
def num():
    pass

