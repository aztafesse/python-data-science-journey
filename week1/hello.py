print("Hello, world!")
print(10%3)
name = "Aziz"
print(type(name))

score =72
if 90 <= score <= 100:
    print("A")
elif 80 <= score <90:
    print("B")
elif 70 <= score < 80:
    print("C")
else:
    print("Needs improvement")

print(10 == 10.0)
print("10" == 10)
print(3 != 3)
print(7 >= 7)
print("abc" < "abd")

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if number_1 > number_2:
    print("First number is greater than the second number")
elif number_1 == number_2:
    print("both numbers are equal")
else:
    print("First number is less than second number")

input_pwd = "password1"

if input_pwd == "secret123":
    print("Access granted")
else:
    print("wrong password")


whatsyourage = 20
if (18 <= whatsyourage <= 65):
    print("True")
else:
    print("False")

x = 10
if x == 10: # x=10 replaced with x == 10
    print ("Ten")

input_name = str(input("What's your name: "))
if input_name.lower() == "aziz":
    print("hello aziz")
else:
        print("hello stranger")

input_number = int(input("Input an integer number"))
if input_number < 0 :
    print("Number is negative")
elif input_number > 0:
        print("Number is positive")
else:
        print("number is zero")

input_year = int(input(" Input year"))
if (input_year%4 == 0 or input_year%400 == 0) and (input_year%100 !=0):
     print("Leap year")
else:
    print("Not a leap year")
