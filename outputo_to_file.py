#!/usr/bin/python

with open("respuesta.txt", "r") as file:
    first_line = file.readline()

print("Titulo: ", first_line)

with open("respuesta.txt", "r") as file2:
    lines = file2.readlines()[1:]

for line in lines:
    print(line)