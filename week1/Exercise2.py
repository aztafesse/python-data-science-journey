word = "Python"

print(word[2])
print(word[0:6])
print(word[2:6])
print(word[::2])

s = "Hello World"

print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

s = "apple,banana,cherry"
fruit = s.split(",")
print(len(fruit))

name = "Aziz"
age = 20

print(f"My name is {name} and I'm {age} yeras old.")

print("a", "b", "c")
print("a", "b", sep="-")
print("World")

print("Line1\nLine2")

print("Name:\tAziz")

print("She said, \"hi\"")

word = "Python"
print(len(word))

for letter in word:
    print(letter)

for i, letter in enumerate(word):
    print(i,letter)

# Task 1 - Basic string ops
s = "Data Science with Python "
print(s.strip().upper())
print(len(s.strip()))
print((s.strip().upper()[::-1]))

#Task 2 - Name formatter

first_name = input("Enter First Name : ")
last_name = input("Enter Last Name : ")
print(f"Hello {first_name} {last_name} ! Your initials are {first_name.upper()[0]}.{last_name.upper()[0]}.")

#Task 3 - Word counter
a = input("Enter a sentence : ")
print (len(a.strip()))
print(len(a.split()))
print(a.upper())

#Task 4 - Email slicer
your_email = input("Enter your email : ")
print(f"Username: {your_email[0:your_email.find("@")].lower()}")
print(f"Domain: {your_email[your_email.find("@")+1:].lower()}")


#Task 5 - Palindrome check (bonus)
word = input(" Enter a word : ")
if (word.lower() == word.lower()[::-1]):
    print("It's a palindrome")
else:
    print("It's not a palindrome")

