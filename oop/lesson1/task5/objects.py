class Student:
    """this class describes
        the average student"""

    debts_count = 10
    subject_count = 10

    def pass_all_subgects(self):
        self.subject_count = 0

    def pass_one_debt(self):
        self.debts_count -= 1

    def pass_all_debts(self):
        self.debts_count = 0

student = Student()
student.pass_all_debts()
print(student.debts_count)
