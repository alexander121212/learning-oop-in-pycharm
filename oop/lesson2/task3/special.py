class Student:
    """this class describes
        the average student"""

    debts_count = 10

    def pas_one_debt(self):
        self.debtsCount -= 1

    def pass_all_debts(self):
        self.debtsCount = 0

print("the name of the class --> ", Student.__name__)
print("module name --> ", Student.__module__)
print("Dictionary class attributes --> ", Student.__dict__)
print("tuple of base classes in the order they appear -->", Student.__bases__)
print("string class documentation --> ", Student.__doc__)