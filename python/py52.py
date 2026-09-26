""" کلاس های انتزاعی """

# کلاس هایی که به کلیات توجه میکنند و به جريیات کاری ندارند
# کلاس فرزند را مجبور به داشتن متد مدنظر میکند
# قابل نمونه سازی نیستند و فقط برای ارث بردن است
# تا زمانی که کلاس فرزند تمامی متد ها را پیاده سازی نکرده باشد آن هم یک متد انتزاع میباشد

from abc import *

# ماشین ها باید حرکت کنند و بایستند
class Car(ABC):
   
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def stop(self):
        pass




class benz(Car):
      # اجباری
      def move(self):
           print('im Going...')

      # اجباری
      def stop(self):
           print('stoping car...')
           
      # اختیاری
      def smart(self):
           print('im smart car...')          
      