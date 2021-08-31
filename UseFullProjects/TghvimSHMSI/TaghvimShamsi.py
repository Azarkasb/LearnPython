'''Taghvim Shamsi'''
# AZ


class Taghvim:
    def __init__ (self, year, month, day):
        self.monthCounter = [0, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
        self.kabiseCounter = [1, 5, 9, 13, 17, 22, 26, 30]
        self.weekDays = ['شنبه', 'يکشنبه', 'دوشنبه', 'شنبه سه', 'چهارشنبه', 'پنجشنبه', 'جمعه']
        self.monthNames = ['فروردين', 'ارديبهشت', 'خرداد', 'تير', 'مرداد', 'شهريور', 'مهر', 'آبان', 'آذر', 'دي', 'بهمن', 'اسفند']
        self.year = 1
        self.year = year
        self.month = 1
        self.month = month
        self.day = 1
        self.day = day

    def __str__(self):
        return str('%d/%s/%d' % (self.year, self.monthNames[self.month - 1], self.day))

    def __repr__(self):
        return str('%d/%d/%d' % (self.year, self.month, self.day))
    def tommorow(self, number = 1):
        while(number):
            number -= 1
            if self.day == self.monthCounter[self.month]:
                self.day = 1
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1
            else:
                self.day += 1

    def weekday(self):
        newDate = Taghvim(1343, 1, 1)
        weekCounter = 0
        while(not((self.year == newDate.year) and (self.month == newDate.month) and (self.day == newDate.day))):
            newDate.tommorow(1)
            weekCounter += 1
            weekCounter %= 7
        else:
            return(self.weekDays[weekCounter])

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and (year > 0):
            self.__year = year
            if year % 33 in self.__kabiseCounter:
                self.__monthCounter[12] = 30
            else:
                self.__monthCounter[12] = 29

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if isinstance(month, int) and (12 >= month >= 1):
            self.__month = month

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if isinstance(day, int) and (31 >= day >= 1):
            self.__day = day

    @property
    def monthCounter(self):
        return self.__monthCounter

    @monthCounter.setter
    def monthCounter(self, lst):
        self.__monthCounter = lst

    @property
    def kabiseCounter(self):
        return self.__kabiseCounter

    @kabiseCounter.setter
    def kabiseCounter(self, lst):
        self.__kabiseCounter = lst

    @property
    def weekDays(self):
        return self.__weekDays

    @weekDays.setter
    def weekDays(self, lst):
        self.__weekDays = lst

    @property
    def monthNames(self):
        return self.__monthNames

    @monthNames.setter
    def monthNames(self, lst):
        self.__monthNames = lst


t = Taghvim(1399, 9, 15)
