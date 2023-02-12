print ("YOU MUST BE OVER 10 YEARS TO USE THIS SIMPLE CALCULATOR")
" "

name = input("Please enter your name : " )

age = int(input("How old are you : " ))

print ("Hello {0}, thanks for telling us you are {1} years old".format(name,age))

if age < 10:
    print ("Sorry, you are too young to use this simple calculator application...bye!!!")
    exit()

if age >= 10:
   cal = input("Will you like to subtract, add or multiply  :  ")

if cal == "subtract":
     a = int(input("Enter your first number = " ))
     b = int(input("Enter your second number = "))
     print("your answer is = "+" "+str(a-b))

     
if cal == "add":
     a = int(input("Enter your first number = " ))
     b = int(input("Enter your second number = "))
     print("your answer is = "+" "+ str(a+b))
