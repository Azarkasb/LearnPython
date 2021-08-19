'''
Barname baraye chap mosalas, lozi, mosalasKhayam_paskal motanaseb ba n vorodi
'''
# All in one
# AZ
n = int(input('Enter an integer : '))

# 1
for i in range(n - 1, -1, -1):
    print(' ' * i + '*' * (n - i))

# 2
print('next'.center(120, '.'))
np = n//2
for i in range(0, np + 1):
    print(('*' * (i * 2 + 1)).center(n))

for i in range(1, np + 1):
    print(('*' * ((np - i) * 2 + 1)).center(n))

print('next'.center(120, '.'))

# 3
n += 1
ls = [0, 1, 0]
s = ''
x = 0
for i in range(1, n):
    # print
    for j in ls[1:-1]:
        s += str(j) + ' '
    print(s.center(4 * n))
    s = ''
    # next
    for k in range(i + 1):
        x = ls.pop()
        ls.insert(0, (x + ls[-1]))
    else:
        ls.insert(0, 0)
