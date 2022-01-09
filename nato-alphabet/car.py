class Car:
    def __init__(self, **kw):
        super().__init__()
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make='Mercedes', model='ML350')
print(my_car.model)
print(my_car.make)