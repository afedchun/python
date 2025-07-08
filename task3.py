x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
a, b = 12, 5
if a + b:
    print('True')
else:
    print('False')

x = 100
y = 50
print(x and y)

if "cat" == "dog":
    print("prrrr")
else:
    print("ruff")

if False:
    print("Nissan")
elif True:
    print("Ford")
elif True:
    print("BMW")
else:
    print("Audi")
if 2 == 2:
    print("ice cream is tasty!")
if 5 > 10:
    print("fan")
elif 8 != 9:
    print("glass")
else:
    print("cream")

x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

x = 5
if x > 0:
    x += 1
if x < 10:
    x +=1
else:
    x -= 1
print(x)
num1 = 10
num2 = 20
result = num1 if num1 < num2 else num2
print(result)

x = 5
if x < 10:
    x += 1
    if x < 5:
        x += 2
x -= 1
print(x)

num = 7 
result = "Even" if num % 2 == 0 else "Odd"
print(result)

x = 10
y = 5

if x > y:
    result = x + y
else:
    result = x - y
print(result)

x = 42

if x > 40 and x < 50:
    if x % 2 == 0:
        print("A")
    elif x % 3 == 0:
        print("B")
else:
    print("C")

x = 20 
y = 10
if x > y and x != 10 and (y % 2 == 0 or x % 4 == 0):
    print("A")
else:
    print("B")

x = 10
match x:
    case int(value):
        if value < 0:
            print("Negative integer")
        else:
            print("Non-negative integer")
    case str(value):
        print("String value")
    case _:
        print("Other type")
        