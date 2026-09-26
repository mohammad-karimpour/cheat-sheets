# first class  - callback function
# ارسال تابع به عنوان ورودی به تابعی دیگر

def num():
    print('****')


def user(num):
    print('------') 
    num()
    print('------')

user() # ------
       # ****
       # ------       