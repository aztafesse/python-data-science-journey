text = "False"
if text:
    print("This runs!")

age = 17
status = "Adult" if age >=18 else "Minor"
print(status)

# Task 1 - Grade calculator
score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Task 2 - Login system

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin"and password == "1234":
    print("Access granted")
else:
    print("Access denied")

# Task 3 - Leap year
year = int(input("Enter a year: "))
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Task 4 - Number classifier
number = int(input("Enter a number: "))
if number == 0:
    print("Zero")
elif number > 0:
    print("Positive even number" if number % 2 == 0 else "Positive odd number")
else:
    print("Negative even number" if number % 2 == 0 else "Negative odd number")

#Task 5 - Ticket price
age = int(input("Enter your age: "))
if age < 5:
    print("Free ticket")
elif 5<= age <=17:
    print("$10")
elif 18 <= age <= 64:
    print("$20")
else:
    print("$15")

# Task 6 - Bonus: Vowel or consonant
letter = input("Enter a letter: ")
vowel = ["a","e","u","i","o"]
if letter.lower() in vowel:
    print("Input is a vowel")
else:
    print("Input is a consonant")

# Challenge before day 4
pin = int(input("Enter your pin: "))
balance = 500
if pin != 1234:
    print("Invalid PIN!")
else:
    amount = int(input("Withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance :
        print("Insufficient funds")
    else:
        print(f"remaining balance: {balance-withdrawal}")

