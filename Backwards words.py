#Ryan Cox
#20/10/14
#a program that writes inputted words backwards



word = str(input("Please enter a word to be writen backwards: "))
length1 = len(word)
length = length1 - 1
placeholder = 0

for count in range(length1):
    letter = word[placeholder+length]                 
    placeholder = placeholder - 1
    print(letter)
