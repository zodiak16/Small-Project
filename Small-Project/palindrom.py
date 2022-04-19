# Write a function to check if there are palindrome strands

# تابعی بنویسیدکه چک کند رشتهاي پالیندروم هست یا نه
def palindrom(a):
    if a==a[::-1]:
        print("palindrom!!!")
    else:
        print("No palindrom")