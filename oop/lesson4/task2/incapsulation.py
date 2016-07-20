class Student:
    """this class describes
        the average student"""

    debts_count = 10
    _cookies = 100
    __coffee = 10

    def __init__(self, desire_to_learn=True):
        self.desire_to_learn = desire_to_learn

neighbor = Student(False)

print(neighbor.find cookies here)
print(neighbor.find coffee here)