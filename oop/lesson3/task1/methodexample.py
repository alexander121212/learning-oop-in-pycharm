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

    reserved word for functions and methods name of method here(firstAttibuteName, secondAttributeName):
        print(secondAttributeName + " I'am play truant this boring lessons!!!")
student = Student()
student.nameOfNewMethod('Yuuuuuuuuhuuuuuuu!!')
