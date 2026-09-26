""" seter - geter """

# برای گرفتن یا تغیر صفت به صورت غیر مستقیم

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    #geter
    def GetName(self):
        return self.name

    #seter
    def SetName(self,name:str):
        self.name = name    



boy = User('mohammad', 19)
boy.GetName() # => mohammad

boy.SetName('faeze')
boy.GetName() # => faeze