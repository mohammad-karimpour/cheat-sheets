""" property method """

# صدا زدن یک متد اما به شکل یک صفت باهاش رفتار میکنیم
# دو روش(متد پراپرتی - دکوراتور پراپرتی) برای این کار وجود دارد

# ورودی ها
""" property(Getname, Setaname, Deletename, Document) """
# Geter => متدی برای گرفتن مقدار
# Seter => متد برای ست کردن مقدار
# Deleter => به محض حذف نمونه اجرا میشود
# SetDocument => ست کردن داک استرینگ

class propMeth:
    def __init__(self, name):
        self.name = name
        

    #geter
    def Getname(self):
        print('im geter')
        return self.name
    
    #seter
    def Setname(self,newname):
        print('im seter')
        self.name = newname

    #deleter    
    def Deletename(self):
        print('im deleter')
        del self.name

    property(Nget=Getname, Nset=Setname, Ndel=Deletename, doc='hi im class in python')




User = propMeth('mohammad')

User.Getname # => geter
User.Setname = 'sana' # => seter
del User.name # => deleter




###################################################################################

# با دکوراتور هم میتوان انجام داد
# دکوراتور پایه حتما باید روی متد گتر باشد و برای مابقی متد ها از اسم همان گتر استفاده خواهی کرد
class decoratprop:
    def __init__(self, name):
        self.name = name
        

    #geter
    @property
    def name(self):
        print('im geter')
        return self.name
    
    #seter
    @name.setter
    def Setname(self,newname):
        print('im seter')
        self.name = newname

    #deleter
    @name.deleter    
    def Deletename(self):
        print('im deleter')
        del self.name




User_2 = decoratprop('faeze')

User_2.Getname # => geter
User_2.Setname = 'amini' # => seter
del User_2.name # => deleter
