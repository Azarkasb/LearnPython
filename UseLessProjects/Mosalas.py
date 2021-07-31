'''
Barname baraye tashkis noe mosalas bar asas azla
'''
#AZ
a = int(input('Pls enter the first side ... '))
b = int(input('Pls enter the second side ... '))
c = int(input('Pls enter the third side ... '))
if a + b <= c or a + c <= b or b + c <= a:
    print('Impossible')
elif a == b and a == c:
    print('Equilateral Triangle')
elif a == b or b == c:
    if a**2 + b**2 ==c or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print('Isosceles Right Triangle')
    else :
        print('Isosceles Triangle')
elif a**2 + b**2 ==c or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
     print('Right Triangle')
else:
    print('Normal Triangle')
    
    
    
