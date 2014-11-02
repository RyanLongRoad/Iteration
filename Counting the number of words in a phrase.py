#Ryan Cox
#30/10/14
#a program which  the number of words in an inputted phrase

phrase = str(input("Please enter the phrase: "))
total = 1
for words in range(phrase.count (" ")):
    total = total+1

print("The number of words in the phrase is: {0}".format(total))
