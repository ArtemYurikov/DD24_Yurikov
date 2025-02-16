class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.__brand = brand  # Инкапсуляция для защиты атрибута
        self.__model = model  # Инкапсуляция для защиты атрибута
        self.__year = year    # Инкапсуляция для защиты атрибута

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        :return: Сообщение о запуске двигателя.
        """
        return f"{self.__brand} {self.__model} engine started."

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.__class__.__name__}(brand={self.__brand}, model={self.__model}, year={self.__year})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление транспортного средства."""
        return f"Vehicle(brand={self.__brand!r}, model={self.__model!r}, year={self.__year!r})"


class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследуется от класса Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в автомобиле.
        """
        super().__init__(brand, model, year)
        self.doors = doors  # Публичный атрибут

    def start_engine(self) -> str:
        """
        Переопределяет метод запуска двигателя для легкового автомобиля.

        :return: Сообщение о запуске двигателя с дополнительной информацией.
        """
        return f"{super().start_engine()} This car has {self.doors} doors."

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()}, doors={self.doors}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление легкового автомобиля."""
        return f"Car(brand={self._Vehicle__brand!r}, model={self._Vehicle__model!r}, year={self._Vehicle__year!r}, doors={self.doors!r})"


class Truck(Vehicle):
    """
    Класс для грузовых автомобилей, наследуется от класса Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param brand: Марка грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность в тоннах.
        """
        super().__init__(brand, model, year)
        self.capacity = capacity  # Публичный атрибут

    def load_cargo(self, weight: float) -> str:
        """
        Загружает груз в грузовой автомобиль.

        :param weight: Вес груза в тоннах.
        :return: Сообщение о загрузке груза.
        """
        if weight > self.capacity:
            return f"Cannot load {weight} tons. Maximum capacity is {self.capacity} tons."
        return f"Loaded {weight} tons of cargo."

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{super().__str__()}, capacity={self.capacity}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление грузового автомобиля."""
        return f"Truck(brand={self._Vehicle__brand!r}, model={self._Vehicle__model!r}, year={self._Vehicle__year!r}, capacity={self.capacity!r})"


if __name__ == "__main__":
    # Пример использования классов
    car = Car("Toyota", "Camry", 2020, 4)
    print(car)
    print(car.start_engine())

    truck = Truck("Volvo", "FH", 2019, 18.0)
    print(truck)
    print(truck.load_cargo(15.0))
    print(truck.load_cargo(20.0))

    
# Базовый класс Vehicle:
# Имеет конструктор, который инициализирует марку, модель и год выпуска транспортного средства.
# Методы __str__ и __repr__ возвращают строковые представления объекта.
# Метод start_engine запускает двигатель и возвращает сообщение.
# Дочерний класс Car:
# Унаследует от Vehicle и добавляет атрибут doors.
# Переопределяет метод start_engine, добавляя информацию о количестве дверей.
# Переопределяет методы __str__ и __repr__ для отображения информации о легковом автомобиле.
# Дочерний класс Truck:
# Унаследует от Vehicle и добавляет атрибут capacity.
# Вводит новый метод load_cargo, который проверяет, можно ли загрузить указанный вес груза.
# Переопределяет методы __str__ и __repr__ для отображения информации о грузовом автомобиле.


