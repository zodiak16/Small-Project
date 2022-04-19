# Write a program that receives the farstname, lastname, unit value, and tens in the input,
# then prints the user's name as the unit number and then the user's surnameas the age tens
# in the output.

#برنامهاي بنویسید که نام ، فامیل ، مقدار یکان و دهگان سن کاربر را در ورودي دریافت کند و سپس به
#ترتیب نام کاربر را به تعداد یکان و سپس فامیل کاربر را به تعداد دهگان سن او در خروجی چاپ نماید

f,l=input().split()
a=int(input("Enter your age: "))
a10= int(a/10)
a1= a%10
for i in range(a1):
    print(f)
for z in range(a10):
    print(l)
    