"""
print("hello world!")

dog = "gir"
cat = "diku"
print("this is my dog's name:", dog, "this is my cat's name:", cat)
"""

"""
num = 12
num2 = 1.2
num3 = "devesh"
value = True
division = "A"
print(num, num2, num3, value, division)
"""
"""
a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
print(a ^ b)
"""
"""
a=10
a+=10
print(a)
a -= 3
print(a)
a *= 4
print(a)
a /= 12
print(a)
a %= 12
print(a)
a **= 12
print(a)
a //= 12
print(a)
b=10
print(a==b)
"""

"""
a = 10
b = 2
print(a != b)
print(a == b)
print(a < b)
print( a > b)
print(a <= b)
print( a >= b)
"""

"""
a = 10
b = 10
if not(a == b & a < b):
    print("chalo ghar chale!!")
elif (a ==b | a<b):
    print("kaam kr kaam!!")
else:
    print("Sahi hai boss!")
"""

"""
TNS Day2:
- Hello World
- Data types (STRING, INT, FLOAT, BOOLEAN, CHAR)
- Operator (Arithmetic Operator - ADD,SUB,DIV,MOD,MUL,EXPONENT) (Assignment Operator - [=,==,<,>,!=]) (Comparison Operator - ==,!=,<=.>=,*=) (Logical Operator - &, |)
"""

"""
a = 10
if(a % 2 == 0):
    print("the number is even")
else:
    print("no it is not")
"""

"""
PASSWORD STRENGTH VALIDATOR -------<>

CODE - 

password = input("Enter your password:")

upper = False
lower = False
digit = False
special = False
special_characters = "!@#$%^&*(),.?\":{}|<>"

if len(password) < 8:
    print("weak password!")
else:
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in special_characters:
            special = True
    
    if upper & lower & digit & special:
        print("AAPKA PASS SURAKSHIT HAI!")
    elif upper | lower | digit | special:
        print("THEEK HAI, CHAL JAYEGA")
    else:
        print("PASSWORD TO DAL DE, ACHA KHASA")
"""


"""
NESTED GRADE EVALUATION WITH ATTENDANCE -------------<>

CODE - 

score = int(input("Enter exam score: "))
attendance = int(input("Enter attendance percentage: "))

if score >= 50 and attendance >= 75:
    print("Pass")
elif score < 50 and attendance < 75:
    print("Fail due to score and attendance")
elif score < 50:
    print("Fail due to score")
elif attendance < 75:
    print("Fail due to attendance")
"""


"""
MULTI-LEVEL LOAN ELIGIBILITY CHECKER --------------<>

CODE - 

age = int(input("Enter applicant age: "))
income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score (300-850): "))

if 21 <= age <= 60 and income >= 2500 and credit_score >= 600:
    print("Loan Approved!")
else:
    if not (21 <= age <= 60):
        print("Rejected due to age")
    if income < 2500:
        print("Rejected due to low income")
    if credit_score < 600:
        print("Rejected due to poor credit")


TRAFFIC FINE CALCULATOR ----------------<>

CODE - 

vehicle_type = input("Enter vehicle type: ")
speed = int(input("Enter speed: "))

speed_limit = 60
over_speed = speed - speed_limit
fine = 0
suspension = False

if over_speed <= 0:
    print("No fine.")
else:
    if vehicle_type == "car":
        if over_speed <= 10:
            fine = 50
        elif over_speed <= 20:
            fine = 100
        else:
            fine = 200
            suspension = True
    elif vehicle_type == "truck":
        if over_speed > 15:
            suspension = True
        if over_speed <= 10:
            fine = 50 * 2
        elif over_speed <= 20:
            fine = 100 * 2
        else:
            fine = 200 * 2
    elif vehicle_type == "motorcycle":
        if over_speed > 25:
            suspension = True
        if over_speed <= 10:
            fine = 50 / 2
        elif over_speed <= 20:
            fine = 100 / 2
        else:
            fine = 200 / 2
    else:
        print("no vehicle found")

    print("Fine:", fine)
    if suspension:
        print("License suspension warning")

"""


