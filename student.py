class Student:
    studcount=0
    def __init__(self,rollnum,name,mark1,mark2):
        self.rollnum=rollnum
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        Student.studcount+=1
    def totalcount(self):
        print"Total number of students",Student.studcount
    def student(self):
        print"Roll number:",self.rollnum,"name:",self.name,"mark1:",self.mark1,"mark2:",self.mark2
        print "total:",self.mark1+self.mark2
stud1=Student(201824,"sandy",80,90)
stud2=Student(201825,"sugan",85,85)
stud3=Student(201823,"manju",84,80)
stud1.student()
stud2.student()
stud3.student()
print "Total students",Student.studcount