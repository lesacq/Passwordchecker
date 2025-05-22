import re

#Asks the user to enter a password
password = input("Enter password: ")

feedback = []

#this checks if the password meets all of the criteria
#making sure its eight characters
if len(password) < 8:
    feedback.append("- Your password must be at least 8 characters long.")

#for containing an uppercase letter
if not any(char.isupper() for char in password):
    feedback.append("- Include an uppercase letter.")

#to ensure that the password contains atleast one digit
if not any(char.isdigit() for char in password):
    feedback.append("- Your password must have atleast a digit.")


if not any(char in "*&^%$#@!" for char in password):
    feedback.append("-A special character must be involved in your pssword(!@#$%^&*).")

# to output if the password is valid or not
if not feedback:
    print("Password is valid.")
else:
    print("Password must:")
    for item in feedback:
        print(item)