# Author: Emanuel Mark Gjoka (AMDG) 3/4/2021

with open('greater_than_20.txt') as lfile2, open('words_without_e.txt', 'w') as sfile2:
    for word in lfile2.readlines():
        if 'e' not in word.strip():
            sfile2.write(word)
            

lfile3 = open('words.txt', 'r')
contents = lfile3.readlines


while True:
    nmrtr = 0
    dnmntr = 0
    for word in lfile3.readlines():
        if 'e' not in word.strip():
            nmrtr += 0
            dnmntr += 1
        else:
            nmrtr += 1
            dnmntr += 1


print(float((nmrtr / dnmntr) * 100))
