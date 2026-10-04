for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0,10,2):
    print(i)

fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(i,fruit)

for i, fruit in enumerate(fruits,start =1):
    print(i,fruit)

names = ["aziz","mayram","hayate"]
ages = [40,4,12]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

count = 0
while count<5:
    print(count)
    count +=1

password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted")

numbers = [1,3,5,7,9]
target = 5
for num in numbers:
    if num == target:
        print("found")
        break
    else:
        print("Not found")

for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})", end=" ")
    print()

for i in range (1,6):
    for j in range(1,6):
        print(f"{i*j:10}", end=" ")
    print()

# Task 1 - Multiplacation table

number = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")

# Task 2 - Sum and average
total = 0
count = 5
for j in range(count):
    num = int(input(f"Enter a number{j+1}: "))
    total += num
print(f" sum: {total}, average: {total/count}")

# Task 3  - FizzBuzz

for i in range(1,51):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)

# Task 4 - Password retry

password = ""
max_attempts = 3
for attempt in range(1, max_attempts+1):
    password = input(f"Enter password (Attempt {attempt}): ")
    if password == "python123":
        print("Access granted")
        break
    elif attempt == max_attempts:
        print("Locked out")

    else:
        print("Wrong password, try again")


# Task 5 - Star pattern

for i in range(1,6):
    print("*"*i)

for i in range(5,0,-1):
    print("*"*i)

# Task 6 - Even numbers only

for i in range(1,31):
    if i%2 ==1:
        continue
    print(i)

# Task 7 - Bonus: Prime number checker
n =int(input("Enter a number: "))
if n < 2:
    print(f"{n} is not a prime number")
else:
    for i in range(2,int(n**0.5)+1):
        print(i)
        print(int(n**0.5 + 1))
        if  n % i == 0 :
            print(f"{n} is not a prime number (divisible by {i})")
            break
    else:
        print(f"{n} is a prime number")    
