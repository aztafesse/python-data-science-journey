fruits =["apple","banana","cherry"]
numbers = [1,2,3,4,5]
mixed = [1, "hello", 3.14, True, None]
empty=[]

#creating list
colors =["red","green","blue"]
nums = list(range(5))
evens = list(range(2,11,2))
letters = list("abc")

zeros=[0]*5

# indexing and slicing

fruits=["apple","banana","cherry","dat","elderberry"]

print(fruits[0])
print(fruits[-1])
print(fruits[1:4])
print(fruits[:2])
print(fruits[3:])
print(fruits[::-1])
print(fruits[::2])

#modifying list

fruits =["apple","banana","cherry"]
fruits[1]="blueberry"
print( fruits)

fruits[0:2] = ["kiwi","mango"]
print(fruits)

# list method
nums=[1,2,3]
nums.append(4)
print(nums)
nums.insert(0,0)
print(nums)

nums.extend([5,6])
print(nums)

nums=[10,20,30,40,20]

nums.remove(20)
print(nums)
last = nums.pop()
print(last)
print(nums)
first=nums.pop(0)
print(first)
print(nums)

nums.clear
del nums 

#finding

fruits=["apple","banana","cherry"]
print(fruits.index("cherry"))
print(fruits.count("banana"))
print("apple" in fruits)
print(len(fruits))

#sorting and reversing

nums=[3,1,4,1,5,9,2,6]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)
nums=[3,1,4,1,5,9,2,6]
sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)

words = ["banana","Apple","Cherry"]
words.sort()
print(words)
words.sort(key=str.lower)
print(words)

nums = [3,1,2]
result = nums.sort()
print(result)
print(nums)

fruits = ["apple","banana","cherry"]

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(i,fruit)

for i in range(len(fruits)):
    print(i,fruits[i])

squares=[]
for i in range(1,6):
    squares.append(i**2)

print(squares)

squares = [i**2 for i in range(1,7)]
print(squares)

evens = [i**2 for i in range(1,21) if i%2==0]
print(evens)

words = ["hi","hello","world","py"]
long_words=[w for w in words if len(w)>4]
print(long_words)

matrix = [[1,2],[3,4],[5,6]]
print(matrix)
flattened = [num for row in matrix for num in row]

print(flattened)

nums = [1,2,3,4,5,6,7]
labels=["even" if n%2 == 0 else "odd" for n in nums]
print(labels)
point =(3,5)

rgb = (255,128,0)
single = (42,)
empty = ()

coords = 3,5

point=(10,20)

def min_max(nums):
    return min(nums), max(nums)

low,high = min_max([3,1,4,1,5])

print(low,high)
print(min_max([3,1,4,1,5]))


# Task 1 - BAsic list ops
mylist = [5,2,8,1,9,3]
print(mylist[0],mylist[-1])
mylist.append(10)
print(mylist)
mylist.remove(2)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)


# Task 2 - Sum without sum()
mylist_nums = [1,2,4,8,5,3,0]
total = 0
for i in mylist_nums:
    total += i
print(total)


#Task 3 - Max without max()
mylist_nums = [1,2,4,8,5,3,0]
maximum = mylist_nums[0]
for i in mylist_nums:
    if i> maximum:
        maximum = i
print(maximum)

# Task 4 - Even filter
mylist =[1,2,3,4,5,6,7,8,9,10]
even = [i for i in mylist if i%2==0]
print(even)

# Task 5 - Squares
mylist = [i**2 for i in range(1,20)]
print(mylist)

# Task 6 - Word lengths
mylist_word =["apple","hi","banana","cat"]
mylist_word_len = [len(i) for i in mylist_word]
print(mylist_word_len)

# Task 7 - Remove duplicates
mylist = [1,2,2,3,4,4,5]
mynewlist = []
for i in mylist:
    if i not in mynewlist:
        mynewlist.append(i)

print(mynewlist)


# Task 8 - Shopping list
mylist =[]
while True:
    new_adding=input("Enter shopping item: ")
    if new_adding.lower() =="done":
        break
    mylist.append(new_adding)
mylist.sort(key =str.lower)
print(f" Your final list is {mylist}, lenght is {len(mylist)}")

# Task 9 - Bonus: Top 3
mylist = [45,12,89,33,67,21,90,8]
mynewlist = sorted(mylist,reverse = True)[:3]

print(mynewlist)

