class Person:
    def __init__(self, pre, mid, fin):
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin
    def Grade(self):
        return (self.__pre + self.__mid + self.__fin) / 3
class Student(Person):
    pass

std1 = Student(90, 90, 90)
std2 = Student(89, 89, 89)
std3 = Student(88, 88, 88)

print("The semestral grade of student1 is:", std1.Grade())
print("The semestral grade of student2 is:", std2.Grade())
print("The semestral grade of student3 is:", std3.Grade())