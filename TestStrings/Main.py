filename = open("list.txt", "r")
namelist = filename.readlines()
llength_2 = len(namelist)
w = 0
while w != llength_2:
    cname = []
    cname = namelist[w]
    cname = cname.split(';')
    llength = (len(cname))
    x = 0
    while x != llength:
        print(cname[x])
        x += 1
    inputn = input("Name: ")
    if inputn in cname:
        print("Valid")
    else:
        print("Invalid")
    print("next \n")
    w += 1

print("end")