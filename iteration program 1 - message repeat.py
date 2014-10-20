#Ryan Cox
#13/10/14
#iteration program 1 - message repeat

message = str(input("Hello, please enter the message you would like be displayed: "))

repeatTimes = int(input("How many times would you like to repeat this message?"))

for count in range(repeatTimes):
    print(message)
