# حلقه while
# تا زمانی که شرط درست باشد حلقه تکرار میشود

num = 0

while num <= 10:
    print(num)
    num += 1
# [1,2,3,4,5,6,7,8,9,10]    


# حلقه تو در تو
while num <= 10:
    print(num)
    while num < 5:
        print("<5")
        num += 1

"""
سه کلمه کلیدی 
break =>  خارج کردن حلقه و توقف کردنش
continue => مختل کردن آن دور از حلقه و ادامه دادن با دور بعدی(آن دور از حلقه را مختل میکند)
else => اگر حلقه بدون مشکل و توقف اجرا شود این دستور هم اجرا میشود
"""   
#  break
while num <= 10:
    print(num)
    num += 1
    if num == 5:
        break   
    #[1,2,3,4,5]


#  continue
while num <= 10:
    num += 1
    if num == 5:
        continue
    print(num)   
    #[1,2,3,4, 6,7,8,9,10]   


#  else
while num <= 10:
    print(num)
    num += 1
else:
    print("OK")    