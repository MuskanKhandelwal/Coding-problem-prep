class Student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        ans1=self.x+other.x
        ans2=self.y+other.y
        return ans1,ans2
S1=Student(10,20)
S2=Student(5,6)
S3=S1+S2 #This will give error as we are trying to add 2 objects, so we will override add method to add objects(operator overloading)
print(S3)
#After operator overloading giving addition answer
#S3=Student.__add__(S1,S2)