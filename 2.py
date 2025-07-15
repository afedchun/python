# number = int(input())
# number = number + 1
# print(number)
# if number % 2 == 0:
#     print("{number} is even")
text = input("text:")
for c in set(text):
    print(f"{c} count:{text.count(c)}")