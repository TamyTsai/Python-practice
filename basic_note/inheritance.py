# 主檔案
# 繼承
from student import Student
student1 = Student("小白",24,"小白國小")
student1.print_school()
student1.print_name()
student1.print_age()

# person.py檔案
class Person:
    def _init_(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


# student.py檔案
from person import Person #人有的特質學生也都有，所以用繼承
class Student(Person): #繼承的類別（被繼承的類別） ，因為 被繼承類別 不存在在這個檔案，所以上一行要先引入
    def _init_(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school

    def print_school(self):
        print(self.school)
