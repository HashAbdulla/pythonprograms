print(f"**** Welcome to the LAB grade calculator! ****")
print()
name=input("Who are we calculating grades for? ==> ")#asking user for name
print()
labsgrade=int(input("Enter the Labs grade? ==> "))#asking user for labs grade
if labsgrade>100: #checking if labs grade is over 100
    print("The lab value should have been 100 or less. It has been changed to 100.") 
    labsgrade=100
if labsgrade<0: #checking if labs grade is less than 0
    print("The lab value should have been zero or greater. It has been changed to zero") 
    labsgrade=0
print()    
examsgrade=int(input("Enter the EXAMS grade? ==> "))#asking user for exams grade
if examsgrade>100: #checking if exams grade is over 100
    print("The exam value should have been 100 or less. It has been changed to 100.")
    examsgrade=100
if examsgrade<0: #checking if exams grade is less than 0
    print("The exam value should have been zero or greater. It has been changed to zero")
    examsgrade=0
print()    
attendance=int(input("Enter the Attendance grade? ==> "))#asking user for attendance grade
if attendance>100: #checking if attendance grade is over 100
    print("The attendance value should have been 100 or less. It has been changed to 100.")
    attendance=100
if attendance<0: #checking if attendance grade is less than 0
    print("The attendance value should have been zero or greater. It has been changed to zero.")
    attendance=0
print()    

               
weightedgrade=(labsgrade*0.7)+(examsgrade*0.2)+(attendance*0.1) #calculating weighted grade
rounded=round(weightedgrade,1)# rounding weighted grade to 1 decimal place
print(f"The weighted grade for {name} is {rounded}") #displaying user's weighted grade

if rounded>=90 and rounded<101: #checking if weightedgrade is an A
    print(f"{name} has a letter grade of A")
      
elif rounded>=80 and rounded<91: #checking if weightedgrade is a B
    print(f"{name} has a letter grade of B")

elif rounded>=70 and rounded<81: #checking if weightedgrade is a C
    print(f"{name} has a letter grade of C")

elif rounded>=60 and rounded<71: #checking if weightedgrade is a D
    print(f"{name} has a letter grade of D")

elif rounded>=0 and rounded<61: #checking if weightedgrade is an F
    print(f"{name} has a letter grade of F")

print()
print(f"**** Thanks for using the Lab grade calculator ****")
    

    
    
