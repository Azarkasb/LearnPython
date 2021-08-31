import TaghvimShamsi as ts
import AZtime as at


class AzDateTime(ts.Taghvim, at.Time):
    def __init__(self, year=1, month=1, day=1, hour=0, minute=0, second=0):
        ts.Taghvim.__init__(self, year, month, day)
        at.Time.__init__(self, hour, minute, second)

    def __repr__(self):
        return str('%d/%s/%d' % (self.year, self.monthNames[self.month - 1], self.day)) + f'\t{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __str__(self):
        return str('%d/%s/%d' % (self.year, self.monthNames[self.month - 1], self.day)) + f'\t{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __iter__(self):
        self.year = 1
        self.month = 1
        self.day = 1
        self.hour = 0
        self.minute = 0
        self.second = 0
        return self

    def __next__(self):
        self.second = (self.second + 1) % 60
        if self.second == 0:
            self.minute = (self.minute+1) % 60
            if self.minute == 0:
                self.hour = (self.hour+1) % 24
                if self.hour == 0:
                    self.day = (self.day + 1)
                    if self.day > self.monthCounter[self.month]:
                        self.day = 1
                    if self.day == 1:
                        self.month = (self.month + 1)
                        if self.month == 13:
                            self.month = 0
                        if self.month == 0:
                            self.month = 1
                            self.year += 1


dt = AzDateTime(1399, 9, 30, 23, 55)
for i in range(60 * 10):
    next(dt)
    print(dt)
