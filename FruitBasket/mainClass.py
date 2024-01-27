
fruits = ["apple", "orange", "mango", "guava"]
basket = []

print("Catch and eat any of these fruits: ", fruits)
basketRange = int(input("How many fruits would you like to catch? "))

for x in range(basketRange):
    choice = input('Fruit ' + str(x + 1) + ' of ' + str(basketRange) + ': ')
    if choice.casefold() == "A".casefold():
        basket.append("apple")
    elif choice.casefold() == "O".casefold():
        basket.append("orange")
    elif choice.casefold() == "M".casefold():
        basket.append("mango")
    elif choice.casefold() == "G".casefold():
        basket.append("guava")

print("Your basket now has: ", basket)

x = 0
while x != 1:
    eat = input("Press E to eat a fruit: ")
    if eat.casefold() == "E".casefold():
        basket.pop()

    if len(basket) != 0:
        print("Fruit(s) in the basket: ", basket)
    elif len(basket) == 0:
        print("No more fruits")
        break