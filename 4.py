#for num in range(2,-5,-1):
#    print(num, end=", ")

#x = 0
#while (x < 100):
 # x+=2
#  print(x)

#for num in range(10, 14):
   #for i in range(2, num):
       #if num%i == 1:
        #  print(num)
         # break

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
  for y in items:
    print(x, y)