print("Input")
string1 = input()
string2 = input()
word = ""
for x in range(len(string1)):
    for y in range(len(string2)):
        if string1[x] == string2[y]:
            length = 0
            while True:
                length += 1
                if len(string1) <= x+length or len(string2) <= y+length:
                    break
                if string1[x+length-1] == string2[y+length-1]:
                    pass
                else:
                    if len(word) > length:
                        break
                    elif length == 1:
                        if len(word) == length:
                            if word == string1[x:(x+length)]:
                                break
                    elif word == "":
                        word = string1[x:(x+length)]
                    elif len(word) < length:
                        word = string1[x:(x+length)]
print(word)