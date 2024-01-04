# 炸雞類別
class FriedChicken:
    # 5個屬性
    def __init__(self, name, flavor, spice_level, sauce, price):
        self.name = name                    
        self.flavor = flavor
        self.spice_level = spice_level
        self.sauce = sauce
        self.price = price

    # 資料輸出
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Flavor: {self.flavor}")
        print(f"Spice Level: {self.spice_level}")
        print(f"Sauce: {self.sauce}")
        print(f"Price: {self.price}")

    # 增加辣度
    def increase_spice_level(self, increment):
        self.spice_level += increment
        print(f"{self.name} spice level increased by {increment}")

    #更換醬料
    def change_sauce(self, new_sauce):
        self.sauce = new_sauce
        print(f"{self.name} sauce changed to {new_sauce}")

    #更新價格
    def update_price(self, new_price):
        self.price = new_price
        print(f"{self.name} price updated to {new_price}\n")

# 建立4個物件
chicken1 = FriedChicken("Spicy Chicken", "Spicy", 5, "Hot BBQ", 10.99)
chicken2 = FriedChicken("BBQ Chicken", "Smoky", 4, "Sweet Chili", 9.99)
chicken3 = FriedChicken("Herb Crusted Chicken", "Savory", 3, "Garlic Parmesan", 12.99)
chicken4 = FriedChicken("Honey Glazed Chicken", "Sweet", 2, "Honey Mustard", 11.99)

# 分別呼叫3個副函式
chicken1.display_info()
chicken1.increase_spice_level(0)
chicken1.change_sauce("Sweet & Sour")
chicken1.update_price(11.69)

chicken2.display_info()
chicken2.increase_spice_level(1)
chicken2.change_sauce("Hot Honey")
chicken2.update_price(12.69)

chicken3.display_info()
chicken3.increase_spice_level(2)
chicken3.change_sauce("Ranch Dressing")
chicken3.update_price(13.99)

chicken4.display_info()
chicken4.increase_spice_level(3)
chicken4.change_sauce("Sweet Soy")
chicken4.update_price(12.59)