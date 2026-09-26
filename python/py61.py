""" متد سیستم(os) """

import os

# اسم سیستم
print(os.name())

# مسیر فعلی
print(os.getcwd())

# تغیر اسم یک پوشه یا فایل
print(os.rename('foo\set','foo\get'))

#لیست پوشه یا فایل های موجود را برمیگرداند
# میتوانید آدرس هم بهش بدهید
print(os.listdir())
print(os.listdir(r'python\seee'))

# ساخت پوشه
print(os.mkdir('soor'))

#تغیر مسیر فعلی
print(os.chdir('../bb/red'))

#حدف یک فایل
print(os.remove(r'ffo\sper.txt'))
# حدف یک پوشه
print(os.rmdir(r'vordem\sfo'))

# نوشتن دستورات cmd
print(os.system('python -v'))
