# def square(a):

#
# def cube(a):
#     return square(a) * a
#
# a = 5
#
# result = cube(a)
# print(result)
#
# count = 0
# list = [2, 4, 56, 8, 3, 4]
# for i in list:
#     if i % 2 == 0:
#         count += 1
#
# print(count)

class Vehicle:
    def __init__(self, color, engine, breaks):
        self.speed = 0
        self.color = color
        self.engine = engine
        self.breaks = breaks


    def info(self):
        print(f'Цвет машины {self.color}')
        print(f'Двигатель {self.engine}')
        print(f'Тормоза {self.breaks}')

    def move(self):
        print(f"Машина двигается со скоростью {self.speed}")

class Car(Vehicle):
    def __init__(self, color, engine, breaks):
        super().__init__(color, engine, breaks)
        self.speed = 100
        # self.color = "Синий"

car = Car("Голубой", 1500, "vip_strong")
car.move()
car.info()