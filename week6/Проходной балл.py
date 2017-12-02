class Student:
    fd = 0
    sd = 0
    td = 0

    def total_points(self):
        return self.fd + self.sd + self.td

    def is_suitable(self):
        return (self.fd >= 40) and (self.sd >= 40) and (self.td >= 40)


inFile = open('input.txt', encoding='utf8')
outFile = open('output.txt', 'w')

budgetPlaces = 0
flag = 0
students = []

for line in inFile:
    if flag == 0:
        budgetPlaces = int(line)
        flag = 1
    else:
        a = line.split()
        st = Student()
        st.fd = int(a[-3])
        st.sd = int(a[-2])
        st.td = int(a[-1])
        students.append(st)

inFile.close()

students.sort(key=lambda x: -x.total_points())

budgetPlacesLeft = budgetPlaces
passPoints = 0
res = -1

maximum = 0
prevMax = 0

for i in students:
    if budgetPlacesLeft > 0:
        if i.is_suitable():
            if i.total_points() > maximum:
                maximum = i.total_points()
            prevMax = passPoints
            passPoints = i.total_points()
            res = passPoints
            budgetPlacesLeft -= 1

    elif budgetPlacesLeft == 0:
        if i.is_suitable() and i.total_points() == passPoints:
            if maximum == i.total_points():
                res = 1
            else:
                res = prevMax
        break


if res == 120:
    res = 0

print(res, file=outFile)

outFile.close()
