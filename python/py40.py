# کار با فایل CSV
# فایلی که جدول مانند است و برای ذخیره داده به کار میرود
# داده ها پشت سر هم به نوشته و با کاما از هم جدا میشوند

# نمونه ای از ساختار فایل
"""
id,name,age,job
1,'mohammad',19,'programmer'
2,'sana',15,'student'
3,faeze,18,'xyat'
4,adel,16,'mekanik'
"""


import csv

# برای دریافت داده از فایل
# دو نوع فرمت برای دریافت وجود دارد

# به همان فرمت فایل(ساده)
with open('numbers.csv', 'r') as num:
    csv.reader(num)

# به صورت دیکشنری 
with open('numbers.csv', 'r') as num:
    csv.DictReader(num) 




# برای نوشتن داده در فایل 
with open('numbers.csv', 'w') as num:
    
    # ابتدا باید شی را باز کنیم
    SetCSV = csv.writer(num)

    # هر بار میتوان فقط یک ستر را 
    SetCSV.writerow(['id','name','age','job'])

    # نوشتن چند ستر(هر آرایه یک ستر)
    SetCSV.writerows([1,'mohammad',19,'programmer'],[2,'sana',15,'student'],[3,'faeze',18,'xyat'])
    
