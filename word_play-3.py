# Author: Emanuel Mark Gjoka (AMDG) 3/4/2021

def avoid(letter):
    counter = 0
    with open('words.txt') as lfile4:
        for word in lfile4.readlines():
            for letter in word:
                if str(letter) in word.strip():
                    counter += 0
                else:
                    counter += 1
    return

lttrs = input('Enter a string containing only letters. ')

print(avoid(lttrs))
