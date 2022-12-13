#Задание 1
class Item:
    def __init__(self, name, price, quantity = 0):
        if self.__check(name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

    def __check(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой")
        if not isinstance(price, (int, float)):
            raise TypeError("Цена товара должна быть числом.")
        if not isinstance(quantity, int):
            raise TypeError("Количество товара должно быть целым числом.")
        else:
            return True

#print(Item('phone', 18000, 5))
# print(Item(18000, 'phone', 5))
# print(Item('phone', '18000', 5))
# print(Item('phone', 18000, 5.5))

#Задание 2

class Phone(Item):
    def __init__(self,name, price, quantity = 0, broken_phone = 0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.broken_phone})"



phone1 = Phone("iPhone 10", 500, 5, 1)
print(phone1)