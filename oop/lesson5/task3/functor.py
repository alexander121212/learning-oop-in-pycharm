class Student:
    """this class describes
        the average student"""

    __slots__ = ['debts_count', 'desire_to_learn']

    def __init__(self, desire_to_learn=True):
        self.desire_to_learn = desire_to_learn

    def call(self):
        print("To study hard!!!!")

student = Student()
print(call it())
