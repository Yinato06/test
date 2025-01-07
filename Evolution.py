class Animal:
    """
    Класс Animal, описывает базовый класс животного
    """
    # Переменная класса, определяет звук, который издает животное
    sound = None

    # Переменная класса, определяет состояние животного (Жизнь)
    live = True

    # Переменная класса, определяет степень опасности животного
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed: int) -> None:
        # Начальная скорость животного определяется при создании
        self.speed = speed

        # Начальные координаты местоположения животного
        self._cords = [0, 0, 0]

    def move(self, dx: int, dy: int, dz: int) -> None:
        """
        Метод для перемещения животного по осям X, Y и Z

        :param dx: смещение по оси X
        :param dy: смещение по оси Y
        :param dz: смещение по оси Z
        """
        # Проверка на возможность погружения под воду
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            # Обновление координат местоположения животного
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self) -> None:
        """
        Метод для получения текущих координат животного
        """
        # Выводит текущие координаты животного
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self) -> None:
        """
        Метод для атаки животного
        """
        # Проверка на степень опасности животного
        if self._DEGREE_OF_DANGER < 5:
            print("I'm Friendly <З")
        else:
            print("I KILL YOU *_*")

    def speak(self):
        """
        Метод для воспроизведения звука, издаваемого животным
        """
        print(f"{self.sound}")


class Bird(Animal):
    """
    Класс птиц. Наследуется от класса Animal. Добавляет новые свойства и методы
    """
    # Переменная класса, определяющая наличие клюва у птицы
    beak = True

    @staticmethod
    def lay_eggs() -> None:
        """
        Статический метод откладывания яиц
        """
        # Генерирует случайное количество яиц
        from random import randint
        eggs_number = randint(1, 4)

        # В зависимости от количества яиц выводит соответствующее сообщение
        if eggs_number == 1:
            print(f"Here is {eggs_number} egg for you")
        else:
            print(f"Here are {eggs_number} eggs for you")


class AquaticAnimal(Animal):
    """
    Класс водных животных. Наследуется от класса Animal. Добавляет новые свойства и методы
    """
    # Определение степени опасности водного животного
    _DEGREE_OF_DANGER = 3

    # Метод погружения животного под воду
    def dive_in(self, dz: int) -> None:
        # Перевод глубины к положительному значению для правильной обработать погружения
        dz = abs(dz)

        # Обновляем координату глубины, учитывая скорость плавания
        self._cords[2] -= (dz * (self.speed // 2))


class PoisonousAnimal(Animal):
    """
    Класс ядовитых животных. Наследуется от класса Animal. Добавляет новые свойства и методы
    """
    # Определение степени опасности водного животного
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    """
    Класс утконоса. Наследуется от классов: Bird, PoisonousAnimal и AquaticAnimal
    """
    # Определяет звук, который издаёт утконос
    sound = "Click-click-click"


# Создаем экземпляр класса Duckbill(Утконос) со скоростью 10
db = Duckbill(10)

# Выводим информацию о состоянии и поведении утконоса
print(db.live)  # Проверяем, жив ли утконос
print(db.beak)  # Проверяем, есть ли у утконоса клюв
db.speak()  # Звук утконоса
db.attack()  # Проверка на опасность утконоса
db.move(1, 2, 3)  # Перемещение утконоса по осям X, Y и Z
db.get_cords()  # Получение текущих координат утконоса после перемещения
db.dive_in(6)  # Погружение под воду
db.get_cords()  # Получение текущих координат утконоса после погружения
db.lay_eggs()  # Откладывание яиц
