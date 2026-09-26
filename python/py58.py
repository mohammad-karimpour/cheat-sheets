""" API """

# pip install requests

import requests



#------------get--------------
response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')


print(response.url) # آدرس api
print(response.status_code) # گرفتن کد ریسپانس
print(response.request) # نوع ریسپانس  get
print(response.reason) # وضعیت ریسپانس  OK - Not Found
print(response.ok) # ریسپانس درست است؟ True - False
print(response.headers) # هدر ریسپانس
print(response.encoding) # نوع ساختار کد  - utf-8
print(response.json()) # دریافت اطلاعات به صورت جیسان

print(dir(response))
print("#"*180)
print("#"*180)
print("#"*180)




















#------------set--------------

#------------put--------------


#----------delete-------------
