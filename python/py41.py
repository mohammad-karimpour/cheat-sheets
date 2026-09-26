""" کلاس ها """
# کلاس ها یک یک الگو هستند برای نمونه های مختلف
# ما میتوانیم هر چند نمونه از این الگو بسازیم با مقادیر متفاوت
# کلاس ها شامل اتریبیوت(صفات) و متد(رفتار) ها هستند

""" ساخت کلاس """

class Person:
    pass

#########################################################

""" ساخت نمونه از کلاس(شی)"""

P_1 = Person()
P_2 = Person()


#########################################################



"""اتریبیوت ها (صفات)"""

#صفت کلاس
# خارج از متد صفت و رفتار به صورت ساده تعریف میکنیم
class Gatt:
    online = 0
    def __init__(self) -> None:
        pass

# با خود کلاس مستوان به آن دسترسی داشت    
print(Gatt.online)



# برای دادن صفت به هر نمونه
P_1.name = 'mohammad'
P_2.age = 18



# گرفتن صفت
P_1.name # mohammad



# مقدار دهی اولیه صفت ب محض ساخت نمونه
# ایجاد صفت برای نمونه در زمان ساخت
class Att:
    def __init__(self,name,family='karimpour'):
        self.A_name = name
        self.A_family = family  # <= برای نمونه یک صفت میسازد و آن را با ورودی مقدار دهی میکند
        self.A_age = 18

# __init__ به محض ساخت نمونه اجرا خواهد شد
# self اولین ورودی هر متدی(صفت - متد)که به صورت قراردادی اسمش سلف هست دقیقا همان نمونه ای هست که ساختید
# مثال => def __init__(A_1 ,name ,family)
# مابقی ورودی هارا بعد از سلف مینویسیم


# ساخت نمونه
Att_m = Att('mohammad','karimpour')
Att_s = Att('sana','ghamisheh')  #Att_s.A_name = sana




###################################################################



""" ساخت متد(رفتار) """

class Met:

    def FullName(self):
        print('mohammad karipmour')

# self اولین ورودی هر متدی(صفت - متد)که به صورت قراردادی اسمش سلف هست دقیقا همان نمونه ای هست که ساختید
# مثال =>  M_6.FullName() = Met.FullName(M_6)
# مثال => M_7.FullName() = def FullName(M_7)
# مابقی ورودی هارا بعد از سلف مینویسیم

# صدا زدن متد برای نمونه
M_1 = Met()
M_1.FullName() # => mohammad karimpour




# class method
# متد که فقط صفت های خود کلاس را میشناسد

class clme:
    online = 12

    # ورودی اول همان کلاس مد نظر است که به صورت قرار دادی اسمش این است
    @classmethod
    def changeOnline(cls,num:int):
        cls.online = num

clme.changeOnline(16)
clme.online # => 16




#staticmethod
# متد که هیچ ربطی به کلاس و نمونه ندارد
# ورودی اول هیچ وابستگی ندارد و اختیاری است

class staticmtd:
 
    @staticmethod
    def className():
        print(staticmtd.__doc__)







###################################################################


""" یک نمونه کلی """

class User:
    def __init__(self,name,family,age):
        self.name = name
        self,family = family
        self.age = age

    def FullName(self,ids=1):
        print(f'{ids}- my name is {self.name, self.family} and my age is {self.age}')


user_M = User('mohammad','karimpour',19)
user_F = User('faeze','amini',18)

user_F.age  # 18

user_M.FullName(2) # 2- my name is mohammad karinpour and my age is 19
user_F.FullName(5) # 5- my name is faeze amini and my age is 18

