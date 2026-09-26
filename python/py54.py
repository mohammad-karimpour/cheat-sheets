""" context manager """
# کار با متد with
# برای انجام عملیات برای قبل اجرا و بعد اجرای یک دستور
# یک کاری شبیه انالیز مد را میدهد

class cont():
    
    def __enter__(self): # قبل از کد اجرا میشود 
        print('after :::',self.__class__)
        print('#'*20)

    def __exit__(self,Type,Value,traceback):  # بعد از کد اجرا میشود حتی اگر کد به خطا منجر شود
        print(self) # داده مورد هدف را برمیگزداند
        print('(ErrorClass):::',Type) #  کلاس ارور را برنیگرداند
        print('(ErrorType) :::',Value) # علت ارور را برمیگرداند
        print('(out) :::',traceback) # گزارشی از تمام اطلاعات لازم برای حل ارور را برمیگرداند
        # مثلا اگر یک عدد تقسیم برا سفر شود خظا میدهد


with cont() as Co:    
    print(10/0)
