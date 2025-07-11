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

lst = input()

result = []
for element in lst.split(','):
    