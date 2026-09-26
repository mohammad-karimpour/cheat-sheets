""" ساخت و ایجاد ارور """

# ایجاد ارور های سفارشی
try:
   print('...')

except:   
    raise ValueError('No Value is str...')




# میتوان به شاخه ارور هم اشاره کرد
try:
  print(5 / 12)
 
# ارور از این شاخه میباشد 
except Exception as Ex:
    raise ValueError('No Value is str...') from Ex





# ساخت ارور

# هر اسمی دلخواه اما ترجیحا اخر ارور داشته باشد
class UserError(TypeError): # از هر دسته ارور میتوان ارث برد
   def __init__(self,T, mesage):
      self.type = T # نوع ارور
      self.mesage = mesage # متن ارور

      # ارسال متن به کلاس پدر
      super().__init__(self.mesage)





# استفاده
try:
   print(5/0)

except:   
    raise UserError(ValueError,'No Value is str...>>>')






# ساخت هشدار(warning)
import warnings

# ورودی دوم اختیاری
warnings.warn('warnig... is not str !!!', TypeError)