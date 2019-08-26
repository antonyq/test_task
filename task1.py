palindrom = lambda str1, str2: str1 == str2[::-1]
anagram = lambda str1, str2: sorted(str1)== sorted(str2)

str1, str2 = 'ароза упаланалапу азора', 'ароза упаланалапу Aзора'

print(anagram(str1,str2))