set = input("Set: ")
k = int(input("k: "))
string = []
for x in set:
    string.append(x)
    for y in range(k):
        for z in set:
            string.append(z);
            print(string)
