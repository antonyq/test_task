from random import randint, random


alphabet = '0123456789' # 'abcdefghijklmnopqrstuvwxyz'
f = open('text.txt', 'w+')

for i in range(1000):
    f.write('\n' if random() < 0.05 else alphabet[randint(0, len(alphabet)-1)])