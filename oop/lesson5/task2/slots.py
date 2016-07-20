class Student:
    """this class describes
        the average student"""

    slot = ['first attr of class', 'second attr of class']

    def __init__(self, desire_to_learn=True):
        self.desire_to_learn = desire_to_learn

    def pass_one_debt(self):
        self.debts_count -= 1

    def pass_all_debts(self):
        self.debts_count = 0

    def play_truant(self, victory_cry):
        print(victory_cry + " I'am playing truant this boring lessons!!!")

student = Student()
student.debts_count = 10
print(student.debts_count, student.desire_to_learn)
