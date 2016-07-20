class Student:
    """this class describes
        the average student"""

    debts_count = 10

    def pass_one_debt(self):
        self.debts_count -= 1

    def pass_all_debts(self):
        self.debts_count = 0


student = Student()

print("the designer ", student.__init__())
print("an object class, an instance of which is the instance ", student.__class__)
print("Dictionary class attributes ", student.__dict__)
print("the hash value of the object of 32-bit numbers ", student.__hash__)
print('removes the attribute', student.__delattr__)
print("assigns the value of the attribute ", student.__setattr__)


