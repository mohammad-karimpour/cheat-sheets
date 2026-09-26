"""  زمان """

#-------------تاریخ---------------


import datetime as dt

# زمان فعلی
print(dt.datetime.now())

# تاریخ امروز
print(dt.date.today())

# تبدیل ثانیه به تاریخ
print(dt.datetime.fromtimestamp(125446854))

# ساخت یک تاریخ
print(Date := dt.date(2022,7,23))
# دستیابی جدا به سال و ماه و روز
print(f'year:{Date.year}- month:{Date.month}- day:{Date.day}')


#-------------ساعت---------------

# ساخت یک ساعت
print(Time := dt.time(12,46,21,103))

# دستیابی جدا به سال و دقیقه و ثانیه و میکرو ثانیه
print(f'hour:{Time.hour}- minutes:{Time.minute}- seconds:{Time.second}- microseconds:{Time.microsecond}')

