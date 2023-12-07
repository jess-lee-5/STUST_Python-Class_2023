class Student:
    # Constructor
    def __init__(self, name, age, student_id, gpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.gpa = gpa

    @property
    def student_name(self):
        print(f'"{self.name}" was accessed.')
        return self.name

    @student_name.setter
    def student_name(self, value):
        print(f'"{self.name}" is now "{value}".')
        self.name = value

    @student_name.deleter
    def student_name(self): 
        print(f'"{self.name}" was deleted')
        del self.name

# Example of usage
if __name__ == "__main__":
    # Creating a new student object
    student1 = Student("Jess Lee", 25, "4A7G0075", 3.8)

    print(student1.student_name)
    student1.student_name = "Peter Pan"
    del student1.student_name
    print(student1.student_name)

class Sports:
    def __init__(self, name):
        self._name = name

    @property
    def sports_name(self):
        return self._name

    @sports_name.setter
    def sports_name(self, value):
        self._name = value

    def practice(self):
        print("Doing Sports practice")

class LandSports(Sports):
    def __init__(self, name, field):
        super().__init__(name)
        self._field = field

    @property
    def landsports_field(self):
        return self._field

    def practice(self):
        print("Doing Land Sports practice")

class WaterSports(Sports):
    def __init__(self, name, activity):
        super().__init__(name)
        self._activity = activity

    @property
    def watersports_activity(self):
        return self._activity

    def practice(self):
        print("Doing Water Sports practice")

# Example of usage
if __name__ == "__main__":
    # Creating a new LandSports object
    baseball = LandSports("baseball", "baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    print(baseball.practice())

    water_skiing = WaterSports("Water Skiing", "Strap on your skis and fly across the water")
    print(water_skiing.sports_name)
    print(water_skiing.watersports_activity)
    print(water_skiing.practice())

    sports = Sports("Softball")
    print(sports.sports_name)
    print(sports.practice())