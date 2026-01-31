#if = do some code only if some condition is true otherwise do something else
age = int(input("Enter your age?: "))

if age>=100:
    print("You are too old for the noise")
elif age >=18:
   print("Welcome to carhub")
elif age<0:
    print("You have mot yet seen a car")
else:
   print("You are too young to know cars")