
import datetime

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

current_time = Time(9, 14, 30)
>>> bread_time = Time(3, 35, 0)
>>> done_time = add_time(current_time, bread_time)
>>> print_time(done_time)


from time import gmtime, strftime
>>> strftime("%Y-%m-%d %H:%M:%S", gmtime())
'2009-01-05 22:14:39'

>>> datetime.datetime.now()
datetime(2009, 1, 6, 15, 8, 24, 78915)

from datetime import datetime
>>> datetime.now().strftime('%Y-%m-%d %H:%M:%S')
