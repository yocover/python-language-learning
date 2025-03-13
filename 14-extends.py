# 继承和多态


class Person:
    """人 class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Student(Person):
    """学生 class"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying.")

    def sleep(self):
        print(f"{self.name} is sleeping in class.")


class Teacher(Person):
    """老师 class"""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching.")

    def sleep(self):
        print(f"{self.name} is sleeping in the classroom.")


class Alex(Person, Student):
    """Alex class"""

    def __init__(self, name, age, grade, subject):
        super().__init__(name, age)
        self.grade = grade
        self.subject = subject

    def study(self):
        print(f"{self.name} is studying in {self.grade} grade.")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


def main():
    p1 = Person("Alice", 20)
    p1.eat()
    p1.sleep()

    stu1 = Student("Bob", 21, 3)
    stu1.eat()
    stu1.study()

    tea1 = Teacher("Charlie", 30, "Math")
    tea1.teach()
    tea1.sleep()


if __name__ == "__main__":
    main()
