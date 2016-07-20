class Student:
    """this class describes
        the average student"""

    debts_count = 10
    dollors = 1000

    def pass_one_debt(self):
        self.debts_count -= 1

    def pass_all_debts(self):
        self.debts_count = 0

student = Student()


print(hasattr(student, 'dollors'))
print(hasattr(Student, 'dollors'))

del Student.dollors

print(hasattr(student, 'dollors'))
print(hasattr(Student, 'dollors'))

print(hasattr(student, 'debtsCount'))
print(hasattr(Student, 'debtsCount'))

delattr(Student, 'debts_count')

print(hasattr(student, 'dollors'))
print(hasattr(Student, 'dollors'))