# print("hello world")
# print('let\'s rock')
# print("raj", "saloni", "nikhil", sep = "-")
# print("raj", "saloni", "nikhil", sep = "\n")

# print("hell\blo RAJ !!")
# print(r"hello\nmr.Raj Aryan")
# print(round(2**0.4, 4))

# name = "Raj"
# last_name = "Aryan"
# age = '21'


# print("hii I am", name, last_name, "and I am", age, "years old" )

# f_name = "Raj"
# l_name = "Aryan"

# full_name = f_name + " " + l_name
# print(full_name * 3)

# name = input("Enter name")
# print("hey" + name)
# age = input("Enter Age")
# print("your age is ", age)

# first_no = int(input("Enter first number"))
# second_no = int(input("Enter second Number"))

# sum = first_no + second_no

# print("Your sum is " + str(sum))

# a = str(50)
# b = float("50")
# c = int("30")

# print(b + c)

# name, age = "Raj", str(22)
# print(name + age)

# name, age = input("Enter your name and age").split(",")
# print(name)
# print(age)

# name = "Raj"
# age = 21

# print("hey {} you are {} years old". format(name, age))

# player = "RONALDO"
# print(player[0])

# player = "MESSI"
# print(player[0:3])

# name = "Raj Aryan"
# print(len(name))
# length = len(name)
# print(length)

# name = "RaJ ArYaN"
# print(name.upper())

# a = "     Raj      "
# b = "!!!..............."

# print(b+a.rstrip())


# name = "Raj aryan is great"

# print(name.replace(" ", "_"))
# name = "Hello hunny bunny raj what are you doing raj"
# print(name.find("raj"))
# a = name.find("raj")
# b = name.find("raj", a+1)
# print(b)

# name = "CONMIGO"
# # 1+7+1 = 9
# print(name.center(9, "*"))

# name = "RAJARYAN"
# # name[1] = "T"
# print(name.replace("R", "T"))

# print(name)

# age = int(input("Enter your age"))

# if age>=18:
#     print("Licence GRanted")

# else:
#     print("Tum abhi chote ho")


# x = 40

# if x>10:
#     print("NUmber is above 10")
#     if x>20:
#         print("Badda hai bhai 20 se bhi bda hai")

#     else:
#         print("not above 20")


# a = 24
# b = 24

# if b>a:
#     print("B is greater than A")
# elif a==b:
#     print("A and B are equal")

# x, y = 8, 8
# if x<y:
#     print("x is less than y")

# elif x==y:
#     print("x is equal to y")

# else:
#     print("x is greater than y")

# age = 30
# if age<18 or age>60:
#     print("Not Eligible")
# else:
#     print("young man")

# name = "Raj"

# if "a" in name:
#     print("A is present in the name")
# else:
#     print("Not present")

# name = input("Enter your name")
# if name:
#     print(f"your name is {name}")
# else:
#     print("please give valif input")

# i = 1

# while i<6:
#     print(i)
#     i= i+1

# i = 1
# while i<=10:
#     print("Raj Aryan")
#     i+= 1

# print the sum of n numbers
# total = 0
# i = 1

# while i<=10:
#     total = total + i
#     i += 1
#     print(total)

# for x in range(2,30, 3):
#     print(x)

# for i in range(10):
#     print(f"Raj: {i}")

# total = 0
# for i in range(1, 11):
#     total +=i
#     print(total)

# n = int(input("enter your number"))
# total = 0
# for i in range(1, n+1):
#     total += i
#     print(total)

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# name = "Raj Aryan"

# for i in "Raj":
#     print(i)

# def fun():
#     print("This is the function")

# fun()

# def sum(a, b):
#     return a+b
# total = sum(5,5)
# print(total)


# def sum(a, b):
#     return a + " " + b
# a = input("input the first name")
# b = input("input the second name")

# total = sum(a,b)
# print(total)

# def addNumbers(a, b):
#     print(a+b)

# addNumbers(5, 5)

# def hii():
#     print("hello guys")
# hii()


# name = "Raj"
# def last(n):
#     return n[1]

# print(last(name))

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#          if n % i == 0:
#             return False

#     return True


# def odd_even():
#     while True:
#         num = int(input("Enter a Number"))
#         if is_prime(num):
#             print("Number is Prime")
#         elif num%2 == 0:
#             print("Number is Even")
#         else:
#             print("Number is Odd")

# print(odd_even())

# def greater(a, b):
#     if a>b:
#         return a
#     else:
#         return b

# num1 = int(input("enter number 1"))
# num2 = int(input("enter number 2"))

# great = greater(num1, num2)
# print(f"{great} is greater")

# def greatest(a, b, c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return c
#     else:
#         return c

# print(greatest(40, 50, 60))


# def greater(a, b):
#     if a> b:
#         return a
#     else:
#         return b

# def new_greatest(a, b, c):
#     great = greater(a, b)
#     return greater(great, c)

# print(new_greatest(10, 20, 30))

# palindrome

# def palindrome(word):
#     reverse = word[::-1]
#     if word==reverse:
#         return True
#     else:
#         return False

# print(palindrome("arora"))
# print(palindrome("horse"))


# word = "hello"
# print(word[::-1])


#  default parameter
# def user_info(firstname, lastname, age = 21):
#     print(f"Your first name is {firstname}")
#     print(f"Your last name is {lastname}")
#     print(f"Your age name is {age}")

# user_info("Raj", "Aryan")

# list

# numbers = [1, 2, 3, 4]
# print(numbers[2])

# mixed = [1, 2, 3, 4, "Raj", "Aryan", 2.5]
# mixed[1] = "two"
# print(mixed)


# def calculate_exp(exp):
#     total = 0
#     for i in exp:
#         total+=i
#     return total

# raj_exp_list = [500, 450, 100]
# renu_exp_list = [100, 500, 120]

# raj_exp = calculate_exp(raj_exp_list)
# print(raj_exp)

# renu_exp = calculate_exp(renu_exp_list)
# print(renu_exp)
