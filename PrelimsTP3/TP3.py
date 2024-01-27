def find_sum(num):
    rep = 1
    result:int=0
    while rep <= num:
        result = result+rep
        rep = rep + 1
    return result

toGet = int(input("Enter a number: "))
print("The sum of the first", toGet, "integers is", find_sum(toGet))