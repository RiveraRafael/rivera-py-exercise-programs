
from collections import deque

movies = deque([])
snacks = deque([])

for i in range(3):
    movies.append(input('Enter movie '+ str(i+1) +' of 3: '))
    i = i+1

for i in range(3):
    snacks.append(input('Enter snack '+ str(i+1) +' of 3: '))
    i = i+1

print("Movies to watch are: ")

for i in movies:
    print("\t"+i)

print("Snacks available are: ")
for i in snacks:
    print("\t"+i)

x = 1

print("Press S each time you finish a snack")
while x != 0:
    inp = input()

    if (inp.casefold() == "S".casefold()):
        snacks.popleft()
        for i in snacks:
            print("\t" + i)

    if (len(snacks)==0):
        print("No more snacks")
        break
