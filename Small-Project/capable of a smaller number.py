#Write a program that receives 2 numbers and checks whether a larger number 
# is capable of a smaller number or not

#برنامھای بنویسید که ٢ عدد دریافت کند وچک کندعدد بزرگترتوانی ازعدد کوچکترھست یا نه

import math
numbers = list(map(int,input().split()))
j,h=sorted(numbers)
a=math.log(h,j)
if a==int(a) :
    print("Yes!!!")
else:
    print("No!!!")
