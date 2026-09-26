"""" متد call در کلاس """

# نمونه هایی که میسازید اگر فراخوانی کنید این متد کال  فراخوانی میشود 


class callclass:
    def __init__(self,name):
        self.name = name

    def __call__(self,age):
        print(f'im {self.name} and {age}')





P_1 = callclass('mohammad')
P_1(18) # => im mohammad and 18


P_2 = callclass('sana')
P_2(15) # => im sana and 15