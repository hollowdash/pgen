import random
import secrets
import string
password = ""

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
            password = "".join(secrets.choice(string.ascii_lowercase) for _ in range(charAmount))
        case 2:
            password = "".join(secrets.choice(string.ascii_letters) for _ in range(charAmount))
        case 3:
            password = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(charAmount))
        case 4:
            password = "".join(secrets.choice(string.hexdigits + string.punctuation) for _ in range(charAmount))
        case None:
            print("Password type empty. Choosing default...")
            password = "".join(secrets.choice(string.hexdigits + string.punctuation) for _ in range(charAmount))
        case _:
            print("Invalid choice. Choosing default...")  
            password = "".join(secrets.choice(string.hexdigits + string.punctuation) for _ in range(charAmount))
    print(password)
main()