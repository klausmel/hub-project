#!/usr/bin/env python3

from sys import argv
from nbr_list import include_nbr

msg = input("send me a letter -> ")
list = []
x = y = i = 0
letter = 97

for i in range(26):
    list.append([0]*2)

for i in range(26):
    for q in range(2):
        list[y][x] = chr(letter)
        include_nbr(list)
    y += 1
    letter += 1

for i in range(26):
    if list[i][0] == msg:
        print("la clave es : ", list[i][1])
    i += 1


#print(list)