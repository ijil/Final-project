#Jill Lee
#Feb 22, 2011
#This program takes in letter grades from the user and calculates the GPA.
#Updated March 19

print("Enter letter grades to get GPA. Enter an asterisk(*) when you're done. Enter Q to quit.")

#Inspired by Dave helping another student during Unclass
sum=0
count=0
grades_list=[]
x=input("Enter a letter grade: ").upper()

while x!='Q':
    if x=='*': #When an asterisk is entered, the results are shown and variables are reinitialized to restart the loop.
        if count==0:
            print("No grades were entered.")
        elif count==1:
            print("GPA is", str(round(sum/count,2))+".\n1 grade was entered.")
        else:
            print("GPA is", str(round(sum/count,2))+".\n"+str(count),"grades were entered.")
        sum=0
        count=0
        x=input("Enter a letter grade (Q to quit): ").upper()
    else: #Adding up grades
        if x=='A':
            sum=sum+4.0
            count=count+1
        elif x=='B':
            sum=sum+3.0
            count=count+1
        elif x=='C':
            sum=sum+2.0
            count=count+1
        elif x=='D':
            sum=sum+1.0
            count=count+1
        elif x=='F':
            sum=sum
            count=count+1
        else: #When neither a letter grade nor Q or * is entered, the program prints an error.
            print("Please enter a valid letter grade(A, B, C, D, or F). Enter an asterisk(*) if you're done.")
        x=input("Enter a letter grade: ").upper()

print("Good bye!")
