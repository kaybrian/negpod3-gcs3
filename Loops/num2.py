#!/usr/bin/python3
letter = input("Input: ").lower().strip()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

for i in letter:
    if i not in vowels:
        print(i, end=", ")
    else:
        continue
