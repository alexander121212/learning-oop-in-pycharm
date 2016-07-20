class Student:
    """this class describes
        the average student"""

    debts_count = 10

    def pass_one_debt(self):
        self.debts_count -= 1

    def pass_all_debts(self):
        self.debts_count = 0


student1 = Student()
print("Has instance Pasha new attribute? ", hasattr(student1, 'freeTime'))

Student.free_time = 0
print("Has object of the class Student new attribute? ", hasattr(Student, 'free_time'))

student2 = Student()
print("Has instance Natasha added attribute? ", hasattr(student2, 'free_time'))

student2.diligent_student = True
print("Has instance Natasha added attribute? ", hasattr(student2, 'diligent_student'))
print("Has object of the class added attribute? ",  hasattr(Student, 'diligent_student'))
