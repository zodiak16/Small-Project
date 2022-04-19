# Write a program that receives 3 numbers from the input and prints the smallest of them.

# برنامھای بنویسید که ٣ عدد از ورودی دریافت کند و کوچک ترین آن ھا را چاپ کند. (به دو روش حل شود

### v1

x=int(input("Enter frist  number: "))
y=int(input("Enter Second  number: "))
z=int(input("Enter thrid number: "))
if x<y:
    if x<z:
        print(x)
if y<x:
    if y<z:
        print(y)
if z<x:
    if z<y:
        print(z)