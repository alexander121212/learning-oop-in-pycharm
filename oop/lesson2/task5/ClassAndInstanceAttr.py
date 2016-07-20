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


print(hasattr(Student, 'desireToLearn'))
print(hasattr(Student, 'debtsCount'))

student1 = Student(False)
print(hasattr(student1, 'desireToLearn'))
print(hasattr(student1, 'debtsCount'))

student2 = Student(True)
print(hasattr(student2, 'desireToLearn'))
print(hasattr(student2, 'debtsCount'))