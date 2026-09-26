"""  json کار با """

# تفاوت های اساس فرمت پایتون با جیسان
#    | python |   =>   | Json |
#  int,flo,comp   =>    Number
#    True,False   =>    true,false
#       none      =>    Null
#       dict      =>    object
#    list,tuple   =>    Array
 







import json

# کار با فرمت جیسان در استرینگ
# یک داده از نوع استرینگ که داخلش کد های جیسان هست و از قانون جیسان پیروی میکند
js_format_str = '{"name": "mohammad" , "age":18}'

# تبدیل جیسان به فرمت پایتون(اسخراج داده از استرینگ)
json.loads(js_format_str)

# تبدیل پایتون(دیکشنری) به فرمت جیسان در قالب استرینگ
json.dumps({'name': None}) # => name: Null






# کار با فرمت جیسان در فایل جیسان
# تبدیل جیسان به فرمت پایتون (استخراج داده از فایل جیسان)
with open('user.json', 'r') as user:
    json.load(user)

# تبدیل پایتون(دیکشنری) به فرمت جیسان برای فایل جیسان
with open('person.json', 'a') as person:
    json.dump({'name': True}, person)    