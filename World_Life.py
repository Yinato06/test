class World:
    """
    Base class World with common attributes: name, life
    """

    def __init__(self, name: str, life: bool) -> None:
        self.name = name
        self.life = life

    def living(self):
        """
        Check if the object is alive.
        """
        return self.life


class Animal(World):
    """
    Animal class, animal with the attribute: hunger.
    """

    def __init__(self, name: str, life: bool, hungry: bool) -> None:
        super().__init__(name, life)
        self.hungry = hungry

    def fed(self):
        """
        Check if the object is alive.
        """
        return self.hungry

    def eat(self, food):

        if food.edibility:
            print(f'{self.name}: eats {food.name}.')
            food.life = False
            self.hungry = False

        else:
            print(f"{self.name}: tries to eat {food.name}, but it's not edible.\n{self.name} died.")
            self.life = False
            food.life = False
            self.hungry = True


class Plant(World):
    """
    Plant class, plant with the attribute: edibility.
    """

    def __init__(self, name: str, life: bool, edibility: bool) -> None:
        super().__init__(name, life)
        self.edibility = edibility


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    pass


wolf = Predator('Scary wolf', True, True)
cow = Mammal('Funny cow', True, True)
mushroom = Flower('Fly-agaric', True, False)
orange = Fruit('Fresh orange', True, True)

print(wolf.name)
print(cow.name)
print(mushroom.name)
print(orange.name)

print('')

wolf.eat(mushroom)
cow.eat(orange)

print('')

print(f"{wolf.name} {"is alive" if wolf.living() else "isn't alive"}")
print(f"{wolf.name} {"is hungry" if wolf.fed() else "isn't hungry"}")
print(f"{cow.name} {"is alive" if cow.living() else "isn't alive"}")
print(f"{cow.name} {"is hungry" if cow.living() else "isn't hungry"}")
