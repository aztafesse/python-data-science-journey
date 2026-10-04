# creating dictionaies

person = {"name":"Aziz", "age":25}

empty = {}
empty2 = dict()

pairs = [("a",1), ("b",2),("c",3)]
d= dict(pairs)

print(d)
print(pairs)

keys = ["name","age","city"]
values= ["Aziz","40","Abu Dhabi"]
person = dict(zip(keys,values))

squares = {n:n**2 for n in range(1,6)}
print(squares)

person["age"] = 35
print(person.get("age","N/A"))
del person["city"]
print(person)
removed = person.pop("age")
print(removed)

keys = ["name","age","city"]
values= ["Aziz","40","Abu Dhabi"]
person = dict(zip(keys,values))

for key in person:
    print(key,person[key])

for key, value in person.items():
    print(f"{key}: {value}")

for value in person.values():
    print(value)

# Nested dictionaries
students = {
    "Aziz": {"age":40, "grade": "A", "city": "Ndjamena"},
    "Hassan": {"age":25, "grade": "B", "city": "Abu Dhabi"},
    "Sarah": {"age":30, "grade": "A+", "city": "Dubai"}
}

print(students["Aziz"]["grade"])

for name, info in students.items():
    print(f"{name} is {info["age"]} years old and got grade {info["grade"]}")

words = ["apple","banana","apple","cherry","banana","apple"]
counts ={}

for word in words:
    counts[word] = counts.get(word,0)+1

print(counts)

counts = {}

for word in words:
    counts.setdefault(word,0)
    counts[word] += 1

print(counts)

from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts)
print(counts.most_common(2))

squares = {n: n**2 for n in range(1,6)}
print(squares)

original = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in original.items()}
print(flipped)

person = {"name": "Aziz", "age": 40, "city": "Ndjamena"}
long_keys = {k:v for k,v in person.items() if len(k)>3}
print(long_keys)

prices = {"apple": 1.5, "banana": 0.75}
discounted = {k:round(v*0.9, 3) for k,v in prices.items()}
print(discounted)

# Task 1 - Basic dict ops

student = {"name": "Aziz", "age": 25, "city": "Dubai"}
print(student.keys())
print(student.values())
print(student.items())
student["grade"] = "A"
student["age"] = 26
del student["city"]
print(student)

# Task 2 - Safe access
person = {"name": "Aziz"}
print(person.get("age","Unknown"))
print(person["name"])
print(person.get("email"))

# Task 3 - Word frequency
words = ["apple", "banana", "apple", "cherry","banana", "apple"]
list_count = {}
for word in words:
    list_count[word] = list_count.get(word,0) + 1
print(list_count)

# Task 4 - Grade book 
grades = {"Aziz": 88, "Ali": 92, "Sara": 79, "Omar": 95, "Layla": 85}
print(grades)
for k,v in grades.items():
    print(f'"{k}: {v}"')

average_grade = sum(grades.values())/ len(grades)
print(average_grade)

highest_score = list(grades.values())[0]
highest_score_name = list(grades.keys())[0]

#for i,ves in grades.items():
#    if grades[i]>highest_score:
#        highest_score = grades[i]
#        highest_score_name = i
for name, score in grades.items():
    if score >highest_score:
        highest_score = score
        highest_score_name = name
print(f" Highest_score is {highest_score} obtained by {highest_score_name}")

# Task 5 - Character frequency
word= input("Enter a word: ")
word_dict = list(word)
counts = {}
for cst in word_dict:
    counts[cst] = counts.get(cst,0)+1

print(counts)


# Task 6 - Phone book
phone_book = {"Aziz": "050-1234", "Ali": "050-5678"}
name = input("Enter a name: ")
if name in phone_book:
    print(f"{name}'s phone number is {phone_book[name]}")
else:
    response = input("Do you want to add it in the phone book: ")
    if response == "yes":
        new_phone_num = input("Enter the phone number: ")
        phone_book[name] = new_phone_num

print(phone_book)

# Task 7 - Dict comprehension
nums = [1,2,3,4,5]
#label = ["Even" if i%2 == 0 else "Odd" for i in nums]
#nums_label = dict(zip(nums,label))
nums_label = {n: "Even" if n%2 == 0 else "Odd" for n in nums}

print(nums_label)

# Task 8 - Bonus: Nested data
employees = {
    "E001": {"name": "Aziz", "salary": 5000},
    "E002": {"name": "Ali",  "salary": 6000},
    "E003": {"name": "Sara", "salary": 5500}
}
for k, v in employees.items():
    print(f'{v["name"]} salary is {v["salary"]}')

total_payroll = 0
for k,v in employees.items():
    total_payroll = total_payroll+v["salary"]

print(f"Total payroll is {total_payroll}")

high_paid = 0
for k,v in employees.items():
    if v["salary"]> high_paid:
        high_paid = v["salary"]
        high_paid_employee = v["name"]
        code = k

print(f'{high_paid_employee} is the highest-paid employee with a salary of {employees[k]["salary"]}')