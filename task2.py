def compress(string):
    compressed = ''
    i = 0

    while i < len(string):
        counter = 0
        for j, char2 in enumerate(string[i:]):
            if char2!=string[i]:
                break
            else:
                counter+=1
        compressed += string[i] + str(counter)
        i += counter

    if len(compressed) > len(string):
        return string
    else:
        return compressed


print(compress('aaabbbbccccc'))
    

