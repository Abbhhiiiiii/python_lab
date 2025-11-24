class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print(self.name,"Got an A grade")
        elif self.marks>=75:
           print(self.name,"Got an B grade")
        else:
           print(self.name,"Got an C grade")
S1=Student("Abhi",92)
S2=Student("Aswin",74)
S3=Student("Akash",88)

S1.grade()
S2.grade()
S3.grade()
