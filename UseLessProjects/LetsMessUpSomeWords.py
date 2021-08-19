import random

'''Barname baraye beham rikhtn tartib chand ta
 kalame ya adad ke behesh midim to barname'''
'''AZ
This program gets many word and She will mess up these words
*dictionary/Outputformats/files'''



print('Enter your words and seprate them with Enter you can finish this process by typing iwannaendme')
s = ''
i = 1
ls = []

while(s != 'iwannaendme'):
    s = input(f'{i} : ')
    ls.append(s)
    i += 1
ls.pop()
random.shuffle(ls)
print(ls)
