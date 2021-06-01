#!/usr/bin/env python3

from sys import argv
from nbr_list import include_nbr
from os import listdir
from subprocess import call
import openpyscad as ops

rectangle = ops.Cube([90, 120, 10])
msg = input("send me a letter -> ")
list = []
letter = 97
letter_selected = ''

for i in range(26):
    list.append([0]*2)

include_nbr(list)

for i in range(26):
    for q in range(2):
        list[i][0] = chr(letter)
    letter += 1
    
for i in range(26):
    if list[i][0] == msg:
        print("la clave es : ", list[i][1])
        letter_selected = list[i][1]
    i += 1
  
if (letter_selected[0] == '1'):
    rectangle = rectangle + ops.Sphere(r = 10, fn = 200).translate([30, 90, 10])
if (letter_selected[1] == '1'):
    rectangle = rectangle + ops.Sphere(r = 10, fn = 200).translate([60, 90, 10])
if (letter_selected[2] == '1'):
    rectangle = rectangle + ops.Sphere(r = 10, fn = 200).translate([30, 60, 10])
if (letter_selected[3] == '1'):
    rectangle = rectangle + ops.Sphere(r = 10, fn = 200).translate([60, 60, 10])
if (letter_selected[4] == '1'):
    rectangle = rectangle + ops.Sphere(r = 10, fn = 200).translate([30, 30, 10])
if (letter_selected[5] == '1'):
    rectangle = rectangle + ops.Sphere(r = 10, fn = 200).translate([60, 30, 10])

rectangle.write("test.scad")
print("scad created, converting...")
files = listdir('.')

for f in files:
    if f.find("test.scad") >= 0:            # get all .scad files in directory
        of = f.replace('.scad', '.stl') # name of the outfile .stl
        cmd = 'call (["openscad",  "-o", "{}",  "{}"])'.format(of, f)   #create openscad command
        exec(cmd)
print("stl created")