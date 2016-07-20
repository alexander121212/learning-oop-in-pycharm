class name of descriptor:
  slots = ("food_name",)
  __storage = {}

  def __init__(self, food_name):
      self.food_name = food_name

  def set(self, instance, value):
      self.__storage[id(instance), self.food_name] = value

  def get(self, instance, owner=None):
      if instance is None:
          return self
      return self.__storage[id(instance), self.food_name]


class Student:
    """this class describes
        the average student"""

    debts_count = 10

    food_name = name of descriptor("food_name")

    def __init__(self, food_name=None, desire_to_learn=True):
        self.desire_to_learn = desire_to_learn
        self.food_name = food_name


student = Student("sausage")
print(hasattr(student, 'food_name'))