#Ryan Cox
#13/10/14
#iteration program 2 - password

password = "secret"

enteredPassword = str(input("Please enter the password: "))

while enteredPassword != password:
    enteredPassword = str(input("That is incorrect, please try again: "))
    if password == enteredPassword:
        print("You now have access to the system")
