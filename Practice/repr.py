class obj:
    def __init__(self,a,b):
        self.a =a
        self.b =b

    def __repr__(self):
        return f'in 1 cenima {self.a} and another cinema has{self.b}'

obj1 = obj('hero','hero1')


print(obj1.a)
print(obj1.b)


# class Car:
#     def __init__(self, color, price):
#         self.color = color
#         self.price = price
#
#     def some(self):
#         print('i am not auto')
#
# car1 = Car('Blue', 2202020)
# car2 = Car('Black', 24252424)
#
# print(car1.color)
# print(car1.price)
# print()
# print(car2.color)
# print(car2.price)
