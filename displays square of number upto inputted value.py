#Ryan Cox
#29/10/14
#a program that asks for a number and displays the squares of all the integers between 1 and this number inclusive.

number = int(input("PLease enter a number: "))

while number > 0:
    total = number * number
    print(total)
    number = number - 1
