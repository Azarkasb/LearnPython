'''Barname baraye beham rikhtn tartib chand ta kalame ya adad ke behesh midim to barname'''
#ThisIsaAUselessProgram
'''AZ
This program gets many word and She will mess up these words
*dictionary/Outputformats/files'''

import random

print('Enter your words and seprate them with \'Enter\' you can finish this process by typing iwannaendme')
s = ''
i = 1
l = []
while(s != 'iwannaendme'):
    s = input(f'{i} : ')
    l.append(s)
    i += 1
l.pop()
random.shuffle(l)
print(l)

