"""
Barname baraye shomaresh kalamat gheir tekrari dar matn
"""
#AZ

farhang = '''
Farhang Holakouee (Persian: فرهنگ هلاکوئي born 1 September 1944) is an Iranian psychologist, sociologist
economist and radio personality.
[1] His radio program-hosted in the past by 670 KIRN
and currently by Radio Hamrah[2]-offers relationship advice to callers in Persian.
[3] Dr. Holakouee was born in Shiraz, Iran and currently resides in Los Angeles, California.[4]
'''
print()
print(farhang)

dic = {91 : None, 93 : None, 40 : None, 41 : None, 46 : None, 58 : None, 59 : None, 44 : None, 48 : None, 49 : None, 50 : None,\
51 : None, 52 : None, 53 : None, 54 : None, 55 : None, 56 : None, 57 : None, 45 : None}
fList = (farhang.translate(dic)).split()
#print(fList)
print()
fSet = set(fList)
#print(fSet)
print()
print(len(fSet), ' Word found in the text') 




