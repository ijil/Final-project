#Jill Lee
#March 22, 2011
#Homework 2 Problem 5
#This program takes two values for x in the equation f(x)=4x(1-x) and calculates it for the number of times the user designates.

#This is the function for calculating and printing the answers. 
def function(x,n):
    while True:
        try:
            while x<=0 or x>=1: #This while loop catches inputs that are not greater than 0 or less than 1 and asks the user to fix.
                x=eval(input("Please enter an initial value that is greater than 0 and less than 1: "))
            break
        except:
            pass
        x=eval(input("Please enter an initial value that is greater than 0 and less than 1: "))
    if n==1: #This if statement is put here for correct English grammar.
        print("Initial value",str(x)+",",n,"iteration:")
    else:
        print("Initial value",str(x)+",",n,"iterations:")
    for i in range(n):
):
                x=4*x*(1-x)
        print(x)

#Taking inputs        
print("Enter two initial values greater than 0 and less than 1 for the equation f(x)=4x(1-x).")
while True:
    try:
        x=eval(input("Enter an initial value: "))
        break
    except:
        print("Incorrect input.")

while True:
    try:
        x2=eval(input("Enter another initial value: "))
        break
    except:
        print("Incorrect input.")

while True:
    try:
        n=int(input("How many iterations?"))
        break
    except:
        print("Incorrect input. Make sure to enter an integer")
        
#Running the functions with the inputs
function(x,n)
function(x2,n)
