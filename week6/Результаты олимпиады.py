# В олимпиаде участвовало N человек. Каждый получил определенное количество баллов, при этом оказалось, что у всех участников разное число баллов. Упорядочите список участников олимпиады в порядке убывания набранных баллов.
#
# Формат ввода
#
# Программа получает на вход число участников олимпиады N. Далее идет N строк, в каждой строке записана фамилия участника, затем, через пробел, набранное им количество баллов.
#
# Формат вывода
#
# Выведите список участников (только фамилии) в порядке убывания набранных баллов.


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
