#Write a program that receives n inputs and prints the difference between the largest and smallest (1 <n)

# برنامھای بنویسید که اِن ورودی دریافت کند واختلاف بزرگترین وکوچکترین آنھا راچاپ کند (1<n)

lst1 = [] 
lst1 = [int(num) for num in input("Enter the list num : ").split()]
x=min(lst1)
z=max(lst1)
print(z-x)