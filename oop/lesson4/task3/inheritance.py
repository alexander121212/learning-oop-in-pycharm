class Student:
    """this class describes
        the average student"""

    debts_count = 10

    def __init__(self, desire_to_learn=True):
        self.desireToLearn = desire_to_learn

    def pass_one_debt(self):
        self.debts_count -= 1

    def pass_all_debts(self):
        self.debts_count = 0

    def play_truant(self, victory_cry):
        print(victory_cry + " I'am playing truant this boring lessons!!!")


class StudentOfRadik(inheritable class name):

    def name of new method(self):
        print('zzzzzzzzzzzzzzzzz')

    def play_truant(self, victory_cry):
        print("I don't like play truant, but")
        get parant version(class name, self).nameOfMethod(victory_cry)
        print("and my conscience does not torment me")

student = Student()
student_of_radik = StudentOfRadik()

print(hasattr(student_of_radik, 'desire_to_learn'))
print(hasattr(student_of_radik, 'pass_one_debt'))
print(hasattr(student_of_radik, 'sleep_sweety'))
print(hasattr(student, 'sleep_sweety'))

student_of_radik.play_truant("ufufuffuuf")