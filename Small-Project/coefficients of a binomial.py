# Write a program that, by taking the coefficients of a binomial, prints the answers if it has an answer.
# "answers no". Otherwise message

# برنامهاي بنویسید که با گرفتن ضرایب یک 2 جملهاي، در صورت داشتن جواب، جوابهاي آن را چاپ
# را چاپ کند. "answers no" کند. در غیر این صورت پیام


import math
a=int(input("for ax*2+bx+c: Enter number a: "))
b=int(input("for ax*2+bx+c: Enter number b: "))
c=int(input("for ax*2+bx+c: Enter number c: "))
delta=b*b-4*a*c
z=math.sqrt(delta)
if delta>0:
    answer1=(-b+z)/(2*a)
    answer2=(-b-z)/(2*a)
    print("answer1 is ",answer1, "answer2 is ", answer2)
if delta==0:
    answer=-b/2*a
    print (answer)
# if delta<0:
#     print("no answers!!!")
