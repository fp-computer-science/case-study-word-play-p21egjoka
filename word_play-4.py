# Author: Emanuel Mark Gjoka (AMDG) 3/4/2021

def aim(letters):
    counter = 0
    with open('words.txt') as lfile5:
        for word in lfile5.readlines():
            for letters in word:
                if str(letters) in word.strip():
                    counter += 1
                else:
                    counter += 0
    return

lttrs = input('Enter a string containing only letters. ')

print(aim(lttrs))
