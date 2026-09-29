import random
import string
password = []

def main():
    global password
    rawCharAmountInput = input("How many characters? ").strip()
    match rawCharAmountInput:
        case "":
            print("Character amount empty. Defaulting to 12.")
            charAmount = 12
        case s if s.isdigit():
            charAmount = int(s)
        case _:
            print("Invalid number. Defaulting to 12.")
            charAmount = 12   
    rawPassTypeInput = input("Password Type?\n1. lowercase\n2. Lower/Uppercase\n3. Alphanumeric\n4. Any\n\n")
    match rawPassTypeInput:
        case "":
            print("Password type empty. Choosing default...")
            passType = 4
        case "1" | "2" | "3" | "4":
            passType = int(rawPassTypeInput)
        case _:
            print("Invalid password type. Choosing default...")
            passType = 4
    match passType:
        case 1:
            for i in range(charAmount):
                password.append(random.choice(string.ascii_lowercase))
        case 2:
            for i in range(charAmount):
                password.append(random.choice(string.ascii_letters))
        case 3:
            for i in range(charAmount):
                password.append(random.choice(string.ascii_letters + string.digits))
        case 4:
            for i in range(charAmount):
                password.append(random.choice(string.hexdigits + string.punctuation))
        case None:
            print("Password type empty. Choosing default...")
            for i in range(charAmount):
                password.append(random.choice(string.hexdigits + string.punctuation))
        case _:
            print("Invalid choice. Choosing default...")
            for i in range(charAmount):
                password.append(random.choice(string.hexdigits + string.punctuation))    
    print("".join(password))
main()