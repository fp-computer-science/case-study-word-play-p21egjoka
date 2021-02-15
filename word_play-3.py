# Author: Emanuel Mark Gjoka (AMDG) 2/12/2021

def avoid(letter):
    with open('words.txt') as lfile4, open('forbidden_words', 'w') as sfile3:
        for word in lfile4.readlines():
            if str(letter) in word.strip():
                sfile3.write(word)

lttr = input('What is your least favorite letter in the Latin Alphabet? ')

print(avoid(lttr))
