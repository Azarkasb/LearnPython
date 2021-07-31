'''Barname baraye rasme parcham Amrikaye fased :| '''
#ThisIsaAUselessProgram
#USAflag
##print('★ ☆ ✨ 卐 ⍟ ⋆ ⚝ ⛤ ✪ ✯ ⭐ ⁎ ✡ ٭ ✺ ꙰ ☕ ▅ ▇ _ ')
import time as t

def union(line):
    if line > 9 :
        if line % 2:
            return '▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ '
        else :
            return '_ _ _ _ _ _ _ _ _ _ '
    if line % 2 :
        return '★  ★  ★  ★  ★  ★'
    else :
        return '  ★  ★  ★  ★  ★   '

def flag(line):
    if line % 2:
        return '▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅'
    else :
        return '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'
for i in range(1, 18):
    t.sleep(1)
    print(union(i) + flag(i))
    

