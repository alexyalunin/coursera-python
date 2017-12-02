l = list(map(int, input().split()))

storage = l[0]
numberOfUsers = l[1]
i = 0
listOfUserStorage = []

while i < numberOfUsers:
    listOfUserStorage.append(int(input()))
    i += 1

sortedListOfUserStorage = sorted(listOfUserStorage)
numberOfAllowedUsers = 0


for i in sortedListOfUserStorage:
    storage -= i
    if storage >= 0:
        numberOfAllowedUsers += 1

print(numberOfAllowedUsers)
