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

    def play_truant(self, victory_cry):
        print((victory_cry + " I'am play truant this boring lessons!!! object is %s") % self)

    class method
    def class_play_truant(cls, victory_cry):
        print((victory_cry + " I'am play truant this boring lessons!!! object is %s")%cls)

    static method
    def static_play_truant(victory_cry):
        print(victory_cry + " I'am play truant this boring lessons!!!")

student = Student()
student.play_truant('Yeeeeaaa!')
student.class_play_truant('yeeea')
Student.class_play_truant('yeeehi')

print(student.play_truant)
print(student.class_play_truant)
print(student.static_play_truant)

