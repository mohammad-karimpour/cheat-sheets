# random رندوم
import random

print(random.random()) # عدد رندوم بین 0تا1

print(random.randint(1,10)) # عدد رندوم بین عدد های داده شده

print(random.choice([1,2,3])) # انتخاب رندوم یک آیتم

print(random.sample([1,2,3,4,5],3)) # انتخاب چند آیتم به صورت رندوم و ساخت یک لیست از آیتم های رندوم

print(random.shuffle([1,2,3,4,5])) # چینش رندوم آیتم ها