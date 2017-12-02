class Participant:
    secondName = ''
    points = 0

numberOfParticipants = int(input())

participants = []

for i in range(numberOfParticipants):
    properties = list(input().split())
    p = Participant()
    p.secondName = properties[0]
    p.points = int(properties[1])
    participants.append(p)


participants.sort(key=lambda part: -part.points)

for p in participants:
    print(p.secondName)
