# دیکشنری(آبجکت ها)
#{key : value}

user = {
    "name":"mohammad",
    "age": 19,
    0918:True,
    "wins": [1,2,3,4],
    "tools":{"car":"BMW","paiscl":"boneto"}
}

#دریافت
print(user["age"]) # 19
print(user.get(0918)) # True اگر کلید وجود نداشته باشد خطا نمیدهد.

# برای دراورن از دسته بندی آیتم های یک لیست
print(**{"id":1,"name":"mohammad"})
