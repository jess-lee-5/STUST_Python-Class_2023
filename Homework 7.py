class Student:

    #類別屬性
    schoolName = "南台科大"
    schoolAddress = "南台街1號"

    def __init__(self) -> None:
        pass

    def __init__(self, id, major, credits, gpa, address):
        self.id = id
        self._major = major
        self._credits = credits
        self._gpa = gpa

    def get_schoolName(self):
        return self.schoolName

    def set_schoolName(self, value):
        self.schoolName = value

    def get_schoolAddress(self):
        return self.schoolAddress

    def set_schoolAddress(self, value):
        self.schoolAddress =value

#建立類別為 Student 的物件st1
st1 = Student("4A3B9001", "CSIE", 60, 4.00, "Sample Street")

#呼叫副函式get_schoolName(), get_schoolAddress()
print(st1.get_schoolName())
print(st1.get_schoolAddress())