# 南台資工飲料店 (父類別)
class CSIEBeverage:
    # 4個屬性
    def __init__(self, name, price, ice_level = "", sugar_level = ""):
        self.name = name
        self.price = price
        self.ice_level = ice_level
        self.sugar_level = sugar_level

    # 資料輸出
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Ice Level: {self.ice_level}")
        print(f"Sugar Level: {self.sugar_level}\n")

# 冷飲 (子類別)
class ColdDrink(CSIEBeverage):
    def __init__(self, name, price, ice_level, sugar_level):
        super().__init__(name, price, ice_level, sugar_level)

# 熱飲 (子類別)
class HotDrink(CSIEBeverage):
    def __init__(self, name, price, sugar_level):
        super().__init__(name, price, sugar_level = sugar_level)

# 建立3個飲料物件
iced_lemon_tea = ColdDrink("Iced Lemon Tea", 3.0, "Regular Ice", "Half Sugar")
hot_mocha = HotDrink("Hot Mocha", 6.5, "Slight Sugar")
hot_macchiato = HotDrink("Hot Macchiato", 7.0, "Slight Sugar")

# 顯示飲料資訊
iced_lemon_tea.display_info()
hot_mocha.display_info()
hot_macchiato.display_info()

# 員工類別
class Employee:
    # 3個屬性
    def __init__(self, name, seniority, work_hours):
        self.name = name
        self.seniority = seniority
        self.work_hours = work_hours

    # 查詢員工姓名
    def query_name(self):
        return self.name

    # 查詢員工資歷
    def query_seniority(self):
        return self.seniority

    # 查詢員工工作時數
    def query_work_hours(self):
        return self.work_hours

    # 計算員工月薪
    def calculate_monthly_salary(self, hourly_rate):
        return self.work_hours * hourly_rate

    # 增加員工工作時數
    def increase_work_hours(self, additional_hours):
        self.work_hours += additional_hours

    # 增加員工資歷
    def increase_seniority(self, years):
        self.seniority += years

# 建立員工物件
employee1 = Employee("Jack", 4, 160)
employee2 = Employee("Kevin", 5, 180)
employee3 = Employee("Bob", 3, 170)

# 呼叫副函式
print(employee1.query_name())
print(employee1.query_seniority())
print(employee1.calculate_monthly_salary(10))
employee1.increase_work_hours(10)
print(employee1.query_work_hours())
employee1.increase_seniority(1)
print(employee1.query_seniority())
print("\n")

print(employee2.query_name())
print(employee2.query_seniority())
print(employee2.calculate_monthly_salary(10))
employee2.increase_work_hours(10)
print(employee2.query_work_hours())
employee2.increase_seniority(1)
print(employee2.query_seniority())
print("\n")

print(employee3.query_name())
print(employee3.query_seniority())
print(employee3.calculate_monthly_salary(10))
employee3.increase_work_hours(10)
print(employee3.query_work_hours())
employee3.increase_seniority(1)
print(employee3.query_seniority())
print("\n")