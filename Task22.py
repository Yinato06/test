class House:
    def __init__(self, name_of_the_complex, number_of_floors):
        self.name = name_of_the_complex
        self.floors = number_of_floors

    def go_to(self, new_floor):
        i = 1
        if new_floor > self.floors:
            print(f'*Хм, мне кажется этажа {new_floor} не существует*')
        else:
            import time
            print(f'*Ты находишься на {i} этаже и думаешь подняться на этаж {new_floor}*')
            time.sleep(2)
            while i + 1 <= new_floor:
                print(f'*Ты поднимаешься на {i + 1} этаж*')
                time.sleep(2)
                i += 1
            print(f'*Ты устал, нужен перерыв')

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors

    def __add__(self, value):
        self.floors += value
        return self

    def __radd__(self, value):
        self.floors += value
        return self

    def __iadd__(self, value):
        self.floors += value
        return self


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

# __str__
print(h3)
print(h4)

# __len__
print(len(h3))
print(len(h4))

# __eq__
print(h1 == h2)

# __lt__
print(h1 < h2)

# __le__
print(h1 <= h2)

# __gt__
print(h1 > h2)

# __ge__
print(h1 >= h2)

# __ne__
print(h1 != h2)

# __add__
print(h1 != h2)

# __radd__
print(h1 != h2)

# __iadd__
print(h1, 5)

h1.go_to(5)
h2.go_to(10)
