#Write a program that prints the number of even and odd numbers in a list

#برنامھای بنویسید کھ تعداد اعداد زوج وفرد دریک لیست را چاپ کند 


n=int(input("Enter a number of output: "))
list1=[]
for i in range(n):
    x=int(input("Enter number: "))
    list1.append(x)
count=0
for a in range(n):
    if list1[a]%2==0:
        count+=1
print("number of zoj: ",count, "number of fard",n-count)