""" mixin """
# به کلاسی گفته میشود که صفت ندارد و فقط متد دارد
# و برای افزودن آپشن و ویژگی - توسعه عملکرد - افزودن قابلیت استفاده میشود

class options:
    def radio():
        return 'radio ON'

# هر کلاسی که بخواهیم این قابلیت ها را داشته باشد از این کلاس ارث بری میکند

class car(options):
    pass

class payscel:
    pass

class airs(options):
    pass