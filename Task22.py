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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
