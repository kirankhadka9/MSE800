class Student:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll
        

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll}")
        print()

s1 = Student("Bimal", 40, 110)
s2 = Student("Ram", 20, 111)
s3 = Student("Shyam", 11, 112)

student_list = [s1, s2, s3]

sorted_students = sorted(student_list, key=lambda s: s.age)

# 4. Display the results
print("Students sorted by Roll Number:")
for student in sorted_students:
    student.display()

#To ask for input from the user.
#name=input("Enter the student's name : ")
#age=int(input("Enter the student's Roll : "))
#class_number=input("Enter the student's Age : ")
  
