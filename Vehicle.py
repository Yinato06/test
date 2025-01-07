class Vehicle:
    __COLOR_VARIANTS = ['white', 'black', 'lavender', 'blue', 'yellow', 'gray', 'purple', 'pink']

    def __init__(self, owner: str, __model: str, color: str, __engine_power: int) -> None:
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.color = color

    def get_owner(self):
        print(f'Owner: {self.owner}')

    def get_model(self):
        print(f'Model: {self.__model}')

    def get_color(self):
        print(f'Color: {self.color}')

    def get_engine_power(self):
        print(f'Engine power: {self.__engine_power}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            print(f'New color: {new_color}\n')
            self.color = new_color
        else:
            print(f"Model {self.__model} doesn't have {new_color} color\n")

    def vehicle_info(self):
        print(f'''Model: {self.__model}
Color: {self.color}
Engine power: {self.__engine_power}
Owner: {self.owner}
''')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedor', 'Toyota Mark II', 'blue', 500)

vehicle1.vehicle_info()
vehicle1.set_color('Red')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Alexander'
vehicle1.vehicle_info()
