age = int(input("Enter your age :"))
number = int(input("Enter any number :"))

if(age<=0):
    print("invalid Age")
elif (age>=60):
    print("Senior")
elif (age>=18):
    print("Adult")
elif (age>=13):
    print("Teenager")
else :
    print("child")
    

#if, if else , if elif else 
'''
    decisions
'''

if (number<0) and (number%2 == 0):
    print(f"{number} is negative number and Even")
elif (number<0) and (number%2 != 0):
    print(f"{number} is negative number and Odd")
elif (number>0) and (number%2 == 0):
    print(f"{number} is Positive number and Even")
elif (number>0) and (number%2 != 0):
    print(f"{number} is Positive number and Odd")
else:
    print("number is Zero")
   
   
