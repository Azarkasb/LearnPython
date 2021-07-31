'''Kelass Zaman'''
#AZ
import time
import datetime as dt
class Time:
    def __init__(self, hour = dt.datetime.now().hour, minute = dt.datetime.now().minute, second = dt.datetime.now().second):
        self.hour = 0
        self.hour = hour
        self.minute = 0
        self.minute = minute
        self.second = 0
        self.second = second

    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self, hour):
        if isinstance(hour, int) and 0 <= hour <= 23:
            self.__hour = hour

    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self, minute):
        if isinstance(minute, int) and 0 <= minute <= 59:
            self.__minute = minute

    @property
    def second(self):
        return self.__second
    @second.setter
    def second(self, second):
        if isinstance(second, int) and 0 <= second <= 59:
            self.__second = second

    def secondToTime(self, second):
        resault = Time()
        second %= (24 * 3600)
        resault.hour = second // (3600)
        second %= 3600
        
        resault.minute = second // (60)
        second %= 60
        resault.second = second
        return resault

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    def __abs__(self):
        return self.hour * 3600 + self.minute * 60 + self.second
    def __eq__(self, other):
        return abs(self) == abs(other)
    def __ge__(self, other):
        return abs(self) >= abs(other)
    def __gt__(self, other):
        return abs(self) > abs(other)
    def __le__(self, other):
        return abs(self) <= abs(other)
    def __lt__(self, other):
        return abs(self) < abs(other)
    def __round__(self):
        self.second = 0
        self.minute -= (self.minute % 15)
        return self
    def __add__(self, other):
        number = abs(self) + abs(other)
        print(number)
        return self.secondToTime(number)
    def __sub__(self, other):
        number = abs(abs(self) - abs(other))
        return self.secondToTime(number)
    

#########################################
a = Time()
h = Time(1, 0, 0)
m = Time(0, 1, 0)
s = Time(0, 0, 1)
       
            
    
