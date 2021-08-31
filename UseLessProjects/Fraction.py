'''Kelas Adad Kasri'''
# AZ
import math


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = 0
        self.denominator = 1
        self.numerator = numerator
        self.denominator = denominator
        self.modify()

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, num):
        if isinstance(num, int):
            self.__numerator = num

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, num):
        if isinstance(num, int) and num != 0:
            self.__denominator = num

    def modify(self):
        if self.denominator < 0:
            self.denominator = abs(self.denominator)
            self.numerator *= -1
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 1:
            self.numerator //= gcd
            self.denominator //= gcd

    def __call__(self):
        print('inferno, baby Im the reason why bads so fun, hells so hot oh so')

    def __eq__(self, other):
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator <= self.denominator * other.numerator)

    def __lt__(self, other):
        return (self.numerator * other.denominator < self.denominator * other.numerator)

    def __ge__(self, other):
        return (self.numerator * other.denominator >= self.denominator * other.numerator)

    def __gt__(self, other):
        return (self.numerator * other.denominator > self.denominator * other.numerator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denomerator)

    def __add__(self, other):
        firstButterfly = self.numerator * other.denominator
        secondButterfly = self.denominator * other.numerator
        commonDenominator = other.denominator * self.denominator
        return Fraction(firstButterfly + secondButterfly, commonDenominator)

    def __sub__(self, other):
        _other = Fraction(-1 * other.numerator, other.denominator)
        return self + _other

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __invert__(self):
        return Fraction(-1 * self.numerator, self.denominator)
# def __mod__(self, other):
# return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
#################################


n1 = Fraction(1, 2)
n2 = Fraction(6, 8)
n3 = Fraction(9, -6)
n1()
