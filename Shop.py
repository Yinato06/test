class Product:
    """
    Класс представления продукта
    """

    def __init__(self, name: str, weight: float, category: str) -> None:
        """
        Конструктор класса Product

        :param name: Название продукта
        :param weight: Вес продукта
        :param category: Категория продукта
        """
        self.name = name
        self.weight = weight.__float__()
        self.category = category

    def __str__(self):
        """
        Метод для строкового представления объекта Product.

        :return: "<Название>: <Вес> кг (<Категория>)"
        """
        return f"{self.name}: {self.weight} kg ({self.category})"


class Shop:
    """
    Класс работы магазина
    """
    __file_name = 'products.txt'

    def get_products(self):
        """
        Получение списка всех продуктов из файла.

        :return: Строку со списком всех продуктов через точку с запятой
        """
        with open(self.__file_name, 'r') as file:
            # Читаем файл и заменяем '\n' на '; '
            products_list = file.read().replace('\n', '; ')
        return products_list

    def add(self, *products):
        """
        Добавление новых продуктов в файл

        :param products: Любое количество объектов типа Product
        """
        try:
            with open(self.__file_name, 'r') as file:
                # Создание множества имен уже существующих продуктов
                product_line = {line.strip() for line in file}
        except FileNotFoundError:
            # Если файла нет - создаем пустой
            product_line = ''


        with open(self.__file_name, 'a+') as file:
            for product in products:
                products_str = f"{product.name}: {product.weight} kg ({product.category})"
                if products_str in product_line:
                    print(f'{product.name} already there')
                else:
                    file.write(products_str + "\n")


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3, 'Groceries')
p3 = Product('Potato', 5.50000, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
