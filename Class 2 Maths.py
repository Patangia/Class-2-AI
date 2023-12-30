'''
a=eval(input("Enter the 1st Number = "))
b=eval(input("Enter the 2nd Number = "))
c=a+b
d=a-b
e=a*b
f=b/a
print('Addition = ',c)
print('Substraction = ',d)
print('Multiplication = ',e)
print('Division = ',f)
'''

'''
a=input("Enter your name = ")
c=a.upper()
print(len(c))
'''

'''
ai_description="Atertifical Inerelligence (AI) is trasformaing Industry and Reshaping the AI"
print(ai_description.count("AI"))
'''
# Contdional Formating If then else,
'''
Maths=eval(input(" Enter the Student Maths Number = "))
Physics=eval(input(" Enter the Student Physic Number = "))
English=eval(input(" Enter the Student English Number = "))
Total_Marks=Maths+Physics+English
Percentage=(Total_Marks/300)*100
print(Percentage)

if(Percentage>=90):
    print('A+')
elif(Percentage<90 and Percentage>=80):
    print('A')
elif(Percentage<80 and Percentage>=70):
    print('B')
elif(Percentage<70 and Percentage>=60):
    print('C')
elif(Percentage<60 and Percentage>=50):
    print('D')
else:
    print('Fail')
'''

'''
name=input("Enter the student name = ")
print(name.upper())
math=eval(input("Enter the students maths number = "))
english=eval(input("Enter the students english number = "))
bio=eval(input("Enter the students bio number = "))
physics=eval(input("Enter the students physics number = "))
chemistry=eval(input("Enter the students chemistry number = "))
sindhi=eval(input("Enter the students Sindhi number = "))
total_marks=math+english+bio+physics+chemistry+sindhi
P=(total_marks/600)*100
print(P)

if(P>=90):
    print("A+")
elif(P<90 and P>=80):
    print('A')
elif(P<80 and P>=70):
    print('B')
elif(P<70 and P>=60):
    print('C')
elif(P<60 and P>=50):
    print('D')
else:
    print=('Fail')

print(f"Hello {name} Your total number is {total_marks} and your percentage is {P:.2f}")    

'''

Last_Name=input("Please enter your last Name = ")
First_Name=input("Please enter your First Name = ")
Full_Name(First_Name,Last_Name)
print(Full_Name.upper())