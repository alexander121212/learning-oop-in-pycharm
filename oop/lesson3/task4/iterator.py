class Student:
    """this class describes
        the average student"""

    def __init__(self, list_of_lessons=None):
        if list_of_lessons:
            self.list_of_lessons = list_of_lessons
            self.index = len(self.list_of_lessons)
        else:
            self.list_of_lessons = []

    def itetator(self):
        return self

    def next step of iterator(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.list_of_lessons[self.index]

subjects = ['math', 'programming']
for lesson in Student(subjects):
    print(lesson)
