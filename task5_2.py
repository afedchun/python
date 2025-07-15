# lst = input()
# # #lst2 = ", ".join(list)
# # result = []
# # for i in lst.split(", "):
# #     if i.isdigit():
# #         result.append(int(i))
# #     else:
# #         pass
# # #result = [str(i) for i in result]

# # print(result)




# import math

# lst = input()

# result = []
# elements = lst.split(',')

# for element in elements:
#     element = element.strip() 
#     try:
#         if element.isdigit() or (element.startswith('-') and element[1:].isdigit()):
#             num = int(element)
#             if num >= 0:
#                 result.append(num)
#         elif '.' in element:
            
#             pass
#         else:
            
#             pass
#     except ValueError:
        
#         pass

# print(result)

# lst = input()
# il = list()
# result = []
# for s in lst.split(','):
#     il.append(int(s.strip()))
# for c in set(il):
#     if il.count(c) % 2 != 0:
#         result.append(c)

# print(result)

# lst = input()
# num = int(input())
# li = list()
# result = 0
# fn = 0
# for element in lst.split(','):
#     li.append(int(element.strip()))
# for i in range(len(li)):
#     if li[i] >= num:
#         fn += 1
# r = 100 * fn / len(li)
# result = round(r, 1)
# print(result)

# lst = input()

# result = []
# result1 = []
# num = 0
# elements = lst.split(',')
# for element in elements:
#     result1.append(int(element.strip()))
# num = enumerate(result1)
# for i in num:
#     result.append(i[0] + i[1])
# print(result)

# lst = input()
# n = input()
# n = int(n)
# n = n - 1 
# result = []
# result1 = []
# elements = lst.split(',')
# enum = enumerate(result1)
# for element in elements:
#     result1.append(int(element.strip()))
# if n > len(result1):
#     result = ["None"]
# else:
#     for i in enum:
#         if i[0] > n-1:
#             result1.append(i[1])
#     for i in range(len(result1)-1):
#         if result1[i] < result1[i+1]:
#             result.append(result1[i])
# print(result)
lst = input()
n = int(input())
i_s = lst.split(',')
i_l = []
for s in i_s:
    try:
        i_l.append(int(s.strip()))
    except ValueError:
        pass
i_l.sort()

result = None
if 1 <= n <= len(i_l):
    result = i_l[n - 1] 
else:
    result = None

print(result)