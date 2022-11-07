#!/usr/bin/python3
num = int(input("Please enter a number: "))

for i in range(num):
    if i % 2 != 0:
        print(f'{i}', end=", ")
print(num)
