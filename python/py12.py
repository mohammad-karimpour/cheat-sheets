# f-string
name = "mohammad"
family = "karimpour"
age = 19
maried = False

print(F"my name is {name} - my family is {family} - my age is {age} and maied is {maried}")
# my name is mohammad - my family is karimpour - my age is 19 and maied is False

# برای غیر فعال کردن یکی از آن ها کافیه {{}} بزارید
print(F"im {name}{family} and {{age}}")
# im mohammad karimpour and {age}