# استرینگ ها

string = "mohammad"
string_m = str('faeze')

#  روش چند خطی
string_2 = """
mohammad karimpour
faeze amini
"""



# کلمات کلیدی داخل استرینگ را با \ فعال میکنند
print("mohammad \n karimpour") # میرود خط بعدی
print('faeze \t amini') # یک تب فاصله می اندازد


# برای غیر فعال کردن کلمات کلیدی 
print(r"mohammad \n karimpour") # کلمه کلیدی هیچ تاثیری ندارد



# میتوانید با + رشته هارو به هم وصل کنید و با * ان ها را تکرار کنید
print(string + string_2) # mohammad mohammad karimpour
print(string * 3) # mohammad mohammad mohammad




# دریافت استرینگ با ایندکس دلخواه
# str[گام - تا - از]
print(string[2]) # h
print(string[2:5]) # ham
print(string[0:6:2]) # mhm
print(string[-2]) # a
print(string[:5]) # moham
print(string[2:]) # hammad

# برای معلکوس کردن رشته
print(string[::-1]) # dammahom
