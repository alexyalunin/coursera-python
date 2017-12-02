def bal_sum(z):
    a = z.split()[-3:]
    z = 0
    for d in a:
        if int(d) < 40:
            z = 0
            break
        else:
            z += int(d)
    return z


in_file = open('input.txt', encoding='utf8')

points = []
budgetPlaces = 0
flag = 0

for s in in_file:
    if flag == 0:
        budgetPlaces = int(s)  # к-во мест
    else:
        b = bal_sum(s)
        if b != 0:
            points.append(b)
    flag += 1

points = sorted(points, reverse=True)

in_file.close()

out_file = open('output.txt', 'w')

res = str()
if len(points) <= budgetPlaces:
    res = str(0)
elif points[budgetPlaces] == points[0]:
    res = str(1)
else:
    for j in points[budgetPlaces - 1::-1]:
        if j != points[budgetPlaces]:
            res = str(j)
            break

print(res, file=out_file)
out_file.close()
