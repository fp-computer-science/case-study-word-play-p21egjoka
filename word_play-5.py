# Author: Emanuel Mark Gjoka (AMDG) 3/4/2021

def is_abecedarian(letters):
    nrgnlst = list(letters.splice())
    rgnlst = list(letters.sort())
    counter = 0
    with open('words.txt') as lfile5:
        for word in lfile5.readlines():
            for letters in word:
                if str(letters) in word.strip():
                    return
      
lfile5.open('words.txt', 'r')
print(is_abecedarian(lfile5))
