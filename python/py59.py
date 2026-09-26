""" match case """
# همان سویچ کیس
# شرط برای اعداد
# هر کیسی که مقدارش با شرط مچ مطابقت داشت اجرا میشود

match 15:
    case 12:
        print('12')
    case 15:
        print('15')
 


# میتوانید از (| یا) هم استفاده کنید  
match 15:
    case 12:
        print('12')  
    case 10 | 15:
        print('10  -  15')




# میتوان از اسم مستعار برای گرفتن آن استفاده کرد
match 15:
    case 12:
        print('12')
    case 15 as num:
        print(num + 2)  




# میتوان از شرط هم استفاده کرد
match 15:
    case 12:
        print('12')
    case 15 if 15<16:
        print('yes 15<16') 