# binary_number = input()

# binary_number = list(binary_number)
# i = 0
# while len(binary_number) > i:
#     if binary_number[i] == "0":
#         if i == 0:
#             binary_number[i] = "[False"
#         elif i == len(binary_number):
#             binary_number[i] = "False]"
#         else:
#             binary_number[i] = "False"
#     else:
#         if i == 0:
#             binary_number[i] = "[True"
#         elif i == len(binary_number):
#             binary_number[i] = "True]"
#         else:
#             binary_number[i] = "True"

#     i += 1
# binary_number = ", ".join(binary_number)
# binary_number += "]"
# print(binary_number)

# n = int(input())

# result = 0
# a = str(n)
# for i in range(len(a)):
#     result += int(a[i])
# c = result / len(a)
# b = result % len(a)

# if b > 0:
#     result = c + 1
# else:
#     result = c
# print(int(result))

# word = input()
# word_l = list(word.lower())
# c = 0
# for i in range(len(word_l)):
#     x = i + 1
#     y = len(word_l) - 1
#     while x <= y:
#         if word_l[i] == word_l[x]:
#             c += 1
#         x += 1
# else:
#     if c == 0:
#         print("True")
#     else:
#         print("False")

# word = input()
# word_l = list(word.lower())
# vowels = 0
# for i in range(len(word_l)):
#     if word_l[i] in "aeiou":
#         vowels += 1
# print(vowels)


# decimal = int(input())
# binary = bin(decimal)
# s = str(binary)
# s = s[2:]
# print(s)

list_int = input()
list_int = list_int.split(",")
list_int = [int(i.strip()) for i in list_int]  
print(list_int)
list_float = []
for i in list_int:
    list_float.append(float(i))
print(list_float)

