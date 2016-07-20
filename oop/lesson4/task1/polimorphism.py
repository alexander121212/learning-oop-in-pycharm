class Student:
    """this class describes
        the average student"""

    debts_count = 10

    def __init__(self, desire_to_learn=True):
        self.desire_to_learn = desire_to_learn

    def pass_one_debt(self):
        self.debts_count -= 1

    def pass_all_debts(self):
        self.debts_count = 0

student = Student('Hello Isia!')
print(student.desire_to_learn)
student = Student(10)
print(student.desire_to_learn)
student = Student(15.5)
print(student.desire_to_learn)
student = Student(True)
print(student.desire_to_learn)


def init_with_cheking_attribute(self, desire_to_learn):
    if function very helpful for checking(desire_to_learn, bool):
        Student.desireToLearn = desire_to_learn
    else:
        Student.desireToLearn = False

Student.overrided method = init_with_cheking_attribute

student = Student(15.5)
print(student.desire_to_learn)
