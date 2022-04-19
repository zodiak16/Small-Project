#Write a program that first receives the first number and then the second number in the input and prints the results of the 
# operations of addition, multiplication, subtraction, power, division by the outside part and the remainder of the division of 
# the first number to the second number in order of priority in the output.
#___________________________________________________________________________________________________________
# برنامهاي بنویسید که ابتدا عدد اول و سپس عدد دوم را در ورودي دریافت کند و نتایج عملیاتهاي جمع
#ضرب، تفریق ، توان ، تقسیم خارج قسمت و مقدار باقیمانده تقسیم عدد اول نسبت به عدد دوم را به ترتیب اولویت در خروجی چاپ نماید

x=int(input("Enter first number: "))

y=int(input("Enter second number: "))

print("Addition: ", x+y ,"\n","Multiplication: ", x*y ,'\n',"Subtraction: ", x-y ,
      '\n',"Floor division: " , x//y ,'\n',"Modulus: ", x%y)