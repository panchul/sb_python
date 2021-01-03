
class Student:
    name=""
    enroll=""

    def setStudent(self):
        self.name=input("enter name: ")
        self.enroll=input("enter id: ")

    def showStudent(self):
        print(f"name: {self.name}")
        print(f"id: {self.enroll}")
        

s=[]
n=int(input("enter total number: "))
for i in range(0,n):
    x=Student()
    x.setStudent()
    s.append(x)

print("info for all students:")
for i in s:
    i.showStudent()


