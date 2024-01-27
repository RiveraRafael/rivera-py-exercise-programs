group1 = set([])
group2 = set([])
self = set([])

for i in range(3):
    group1.add(input("Enter birth month " + str(i+1) + ": "))

for i in range(3):
    group2.add(input("Enter birth month " + str(i+1) + ": "))

print("Group 1: " + str(group1))
print("Group 2: " + str(group2))

self.add(input("Enter your birth month: "))

print("Union: " + str(group1|group2))
print("Intersection: " + str(group1&group2))
print("Difference: " + str(group1-group2))

if (group1|group2).__contains__(self.pop()) == True:
    print("You have the same birth month with one of your classmates")
else:
    print("You don't have the same birth month with one of your classmates")
