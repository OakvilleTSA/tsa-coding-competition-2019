roomNumber = int(input("How many rooms are there: "))
roomSizes = []
for x in range(roomNumber):
    roomSize = input("Enter the square footage of room " + str(x + 1) + ": ")
    roomSizes.append(int(roomSize))
roomSizes.sort()
cleanLeft = 5000
roomsCleaned = 0;
for x in roomSizes:
    if (cleanLeft - x >= 0):
        cleanLeft -= x
        roomsCleaned += 1
print(str(roomsCleaned) + " room(s) were cleaned")