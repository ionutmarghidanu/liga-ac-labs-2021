class Student(object):

    def __init__(self, age, height, weight):
        self.age = age
        self._height = height
        self.__weight = weight

    @property
    def height(self):
        print("Entered getter")
        return self._height

    @height.setter
    def height(self, value):
        print("Entered setter")
        self._height = value


student1 = Student(1, 2, 3)

student1.height = 20
print(student1.height)
