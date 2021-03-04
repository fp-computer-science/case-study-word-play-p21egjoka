# Author: Emanuel Mark Gjoka (AMDG) 3/4/2021

with open('words.txt') as lfile, open('greater_than_20.txt', 'w') as sfile:
    for word in lfile.readlines():
        if len(word.strip()) > 20:
            sfile.write(word)

