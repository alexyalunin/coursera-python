str = input()

if str.count('f') == 1:
    print(str.find('f'))
elif str.count('f') >= 2:
    print(str.find('f'), str.rfind('f'))
