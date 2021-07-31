'''Barname baraye mohasebe zaman ejraye tabe bazgashti fib(n) va moghayese zaman dar n haye
mokhtalef

install matplotlib

'''
#AZ
import matplotlib.pyplot as plt
import datetime as dt
import time as time

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)

timeLine = []
ttimeLine = []
now = None
tnow = None
x = None
for i in range(1, 39):
    tnow = time.time()
    now = dt.datetime.now()
    x = fib(i)
    timeLine.append((dt.datetime.now() - now).microseconds)
    ttimeLine.append(1000000*(time.time() - tnow))


plt.plot(timeLine, 'o:r')
plt.plot(ttimeLine, 'o--b')
plt.show()
