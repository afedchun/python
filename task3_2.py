#word = input()

#word_l = word.lower()
#word_x = word_l.count('x')
#word_o = word_l.count('o')
#if word_x == word_o:
#    print("True")
#elif word_o > word_x or word_x > word_o:
#    print("False")
#elif word_x == word_o and word_x == 0 and word_o == 0:
#    print("True")

#number = int(input())


#a = number * -1 if number > 0 else abs(number)
#a = -number
#print(a)

#def s_int(st_in):
#    try:
#        int(st_in)
#        return True
#    except ValueError:
#        return False

#st = input()

#print (int(st)) if s_int(st) == True else print("Not a number")

#print (int(st))
#num1 = int(input())
#num2 = int(input())

#print (True) if a == 10 or b == 10 or a + b == 10 

card = input()

if len(card) < 16 or len(card) > 16 or not card.isdigit():
    print("Invalid card")
else:
    d = card[-15:-11:-1]  # Extract the 4 digits from the end
    d = d[::-1]  # Reverse the extracted digits
    c = 12 * "*"
    card = c + d
    print(card)