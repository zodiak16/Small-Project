#Write a function that receives a list of numbers and returns the average of the members.

# تابعی بنویسید که لیستی از اعداد را دریافت کند و میانگین اعضا را برگرداند.
numbers=list(map(int,input().split(" ")))
def avg(a):
    sum1=sum(numbers)
    len1=len(numbers)
    avg1=sum1/len1
    return avg1
avg(numbers)