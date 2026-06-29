# Student report system


class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    
    

def total(s):
    return sum(s.marks)

def percentage(s):
    return total(s)/len(s.marks)

def grades(s):
    grade=''
    if percentage(s)>=90:
        grade='A'
    elif percentage(s)>=75:
        grade='B'
    elif percentage(s)>=60:
        grade='C'
    elif percentage(s)>=40:
        grade='D'
    else:
        grade='FAIL'
    return grade



l=[Student('Sarvesh',16,[99,75,88]),Student('Sam',17,[59,45,65]),Student('Jameel',5,[20,40,53])]

try:
    with open('student.txt','w') as file:
        for i in range(len(l)):
            file.write('--------------------------------------------------------\n')
            file.write(f'{i+1}: Name of Student is {l[i].name}\n Rollno is {l[i].roll_no}\n His marks are {l[i].marks} \n')
            file.write(f' Total marks are {total(l[i])}\n Percentage are {percentage(l[i])} \n Grades are {grades(l[i])} \n')
            file.write('--------------------------------------------------------\n')

except ValueError:
    print('Please enter valid marks ')




try:
    with open('student.txt','r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('Sorry but students report file cannot be found ')