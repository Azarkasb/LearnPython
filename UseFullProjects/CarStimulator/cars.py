
class Car():
    def __init__(self, color, speed):
        self.colorList = ['orange', 'black', 'blue', 'green', 'colorful', 'yellow', 'red']
        self.color = 'black'
        self.color = color
        self.speed = 0
        self.speed = speed
        self.start = False

    def __repr__(self):
        return f'I am a {type(self).__name__} {self.color} car'

    def __str__(self):
        return f'I am a {type(self).__name__} {self.color} car'

    def turnOn(self):
        self.start = True

    def turnOff(self):
        self.start = False

    @property
    def colorList(self):
        return self.__colorList

    @colorList.setter
    def colorList(self, colorList):
        if isinstance(colorList, list):
            self.__colorList = colorList

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color in self.colorList:
            self.__color = color

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if (isinstance(speed, float) or isinstance(speed, int)) and speed >= 0:
            self.__speed = speed

    @property
    def gearBox(self):
        return self.__gearBox

    @gearBox.setter
    def gearBox(self, gearList):
        if isinstance(gearList, list):
            self.__gearBox = gearList

    @property
    def gear(self):
        return self.__gear

    @gear.setter
    def gear(self, gear):
        if gear in self.__gearBox:
            self.__gear = gear

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        if isinstance(start, bool):
            self.__start = start


class Simple(Car):
    def __init__(self, color, speed):
        super().__init__(color, speed)
        self.gearBox = ['0', 'R', '1', '2', '3', '4', '5']
        self.gear = '0'


class Auto(Car):
    def __init__(self, color, speed):
        super().__init__(color, speed)
        self.gearBox = ['P', 'N', 'R', 'D']
        self.gear = 'P'
