import turtle
import cars
import time

# GlobalVariables

# input
colorList = ['orange', 'black', 'blue', 'green', 'colorful', 'yellow', 'red']
color = input(f'Choose color between  {colorList} : ')
speed = float(input('Choose speed between 0 to 240 : '))
if input('Choose the type of car [auto, simple] : ') == 'auto':
    car = cars.Auto(color, speed)
else:
    car = cars.Simple(color, speed)
# Process
# Ready
screen = turtle.getscreen()
screen.setup(800, 600)
screen.register_shape(f'{color}.gif')

carShape = turtle.Turtle(f'{color}.gif')
carShape.penup()
turtle.hideturtle()
carShape.speed = 10

gear = turtle.Turtle(visible=False)
gear.speed(0)
gear.penup()
gear.goto(-40, 170)
gear.write(f'Gear : {car.gear}')

writer = turtle.Turtle(visible=False)
writer.speed(0)
writer.penup()
writer.goto(-40, 200)
writer.write('Hello')


for i in range(0, 5):
    writer.clear()
    writer.write(str(5 - i).ljust(2) + 'seconds left')
    time.sleep(1)
writer.clear()
writer.write('Start')

# +A
if type(car).__name__ == 'Auto':
    car.gear = 'D'
else:
    car.gear = '1'

gear.clear()
gear.write(f'Gear : {car.gear}')

for i in range(30):
    time.sleep(0.24 - (car.speed / 1000))
    carShape.forward(10)

    if type(car).__name__ == 'Simple':
        if i == 10:
            car.gear = '2'
            gear.clear()
            gear.write(f'Gear : {car.gear}')
        elif i == 17:
            car.gear = '3'
            gear.clear()
            gear.write(f'Gear : {car.gear}')

# -2A
car.gear = 'R'

gear.clear()
gear.write(f'Gear : {car.gear}')

for i in range(60):
    time.sleep(0.24 - (car.speed / 1000))
    carShape.bk(10)

# +A
if type(car).__name__ == 'Auto':
    car.gear = 'D'
else:
    car.gear = '1'

gear.clear()
gear.write(f'Gear : {car.gear}')

for i in range(30):
    time.sleep(0.24 - (car.speed / 1000))
    carShape.forward(10)

    if type(car).__name__ == 'Simple':
        if i == 10:
            car.gear = '2'
            gear.clear()
            gear.write(f'Gear : {car.gear}')
        elif i == 17:
            car.gear = '3'
            gear.clear()
            gear.write(f'Gear : {car.gear}')

# End
if type(car).__name__ == 'Auto':
    car.gear = 'P'
else:
    car.gear = '0'

gear.clear()
gear.write(f'Gear : {car.gear}')
writer.clear()
writer.write('End')
