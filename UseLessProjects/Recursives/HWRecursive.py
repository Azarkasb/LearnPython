'''Tabe (be mim mim) , (jam) va (zarb) be do ravesh adi va bazgashti'''


#GCD
def gcd(x, y):
    c = 0
    while y:
        c = x%y
        x = y
        y = c
    return x

def rgcd(x, y):
##    return (x) if x == y else (return (rgcd(x, x%y))) if x > y else return (rgcd(x, y%x))
    if x == y:
        return x
    elif x > y:
        return(y, x%y)
    else :
        return(y%x, x)
    
#Addition
def addition(x, y):
    for i in range(y):
        x += 1
    return x

def raddition(x, y):
    if not(y):
        return x
    return raddition(x + 1, y - 1)

#multipication
def multiplication(x, y):
    z = 0;
    for i in range(y):
        z += x
    return z

def rmultiplication(x, y):
    if not(y) :
        return 0
    return x + rmultiplication(x, y - 1)
        
######################## # # # # main
a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
ngcd = gcd(a, b)
print(f'gcd ({a} and {b}) = {ngcd}')
nrgcd = rgcd(a, b)
print(f'rgcd ({a} and {b}) = {ngcd}')
naddition = addition(a, b)
print(f'addition ({a} and {b}) = {naddition}')
nraddition = raddition(a, b)
print(f'raddition ({a} and {b}) = {nraddition}')
nmultiplication = multiplication(a, b)
print(f'multiplication ({a} and {b}) = {nmultiplication}')
nrmultiplication = rmultiplication(a, b)
print(f'rmultiplication ({a} and {b}) = {nrmultiplication}')

