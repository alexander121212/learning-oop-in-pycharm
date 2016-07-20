class Student:
    """this class describes
        the average student"""

    subject_count = 10

    def pass_one_subject(self):
        self.subject_count -= 1

    def passAllSubgects(self):
        self.subject_count = 0