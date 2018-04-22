#!/usr/bin/python3
import sys
import random

if len(sys.argv) == 1:
    print("Defaulting to generating a 25 character long password")
    length = 25
else:
    length = int(sys.argv[1])

with open("chars.txt") as f:
    words = f.readlines()

r = random.SystemRandom()
output = []
for i in range(length):
    randindex = r.randrange(len(words))
    output.append(words[randindex].strip())

print(''.join(output))
