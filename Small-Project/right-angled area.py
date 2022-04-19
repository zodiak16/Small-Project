# Write a program that receives the 3 sides of a triangle and prints whether the triangle is
# right-angled or not. If it is right-angled, print its area

# برنامه ای بنویسید که با دریافت کردن ٣ ضلع مثلث، چاپ کند مثلث قائم الزاویه
# ھست یا نه در صورت قائم الزاویه بودن، مساحت آن را چاپ کند

numbers = list(map(int,input().split()))
x,y,z = sorted(numbers)
if x**2 + y**2 == z**2:
    print("It is triangle!!! ")
else:
    print("It is not triangle!!!")