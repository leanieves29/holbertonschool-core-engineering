#!/usr/bin/env python3
letters = ""
for i in range(97, 123):
    if chr(i) != "q" and chr(i) != "e":
        letters += chr(i)
print(letters)
