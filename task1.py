import doctest


class Wood:
    def __init__(self, height_volume: float, width_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param height_volume: Объем стакана
        :param width_volume: Объем занимаемой жидкости

        Примеры:
        >>> wood = Wood(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(height_volume, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height_volume <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height_volume = height_volume

        if not isinstance(width_volume, (int, float)):
            raise TypeError("Ширина дерева должна быть int или float")
        if width_volume < 0:
            raise ValueError("Ширина дерева не может быть отрицательным числом")
        self.width_volume = width_volume
    def is_empty_wood(self) -> bool:
        """
        Функция проверяет, сломано ли дерево

        :return: Является ли дерево сломанным

        Примеры:
        >>> wood = Wood(500, 0)
        >>> wood.is_empty_wood()
        """
        ...


    def remove_a_piece_of_wood(self, estimate_wood: float) -> None:
        """
        Отрубка части дерева.

        :param estimate_wood: Длина дерева
        :raise ValueError: Если длина куска превышает длину самого дерева,
        то возвращается ошибка.

        :return: Длина реально отрубленного куска

        Примеры:
        >>> wood = Wood(500, 500)
        >>> wood.remove_a_piece_of_wood(200)
        """
        ...

class Whale:
    def __init__(self, age_volume: float, weight_volume: float):
        """
        Создание и подготовка к работе объекта "Кит"

        :param age_volume: Возраст кита
        :param weight_volume: Вес кита

        Примеры:
        >>> whale = Whale(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(age_volume, (int, float)):
            raise TypeError("Возраст кита должен быть типа int или float")
        if age_volume <= 0:
            raise ValueError("Возраст кита должен быть положительным числом")
        self.age_volume = age_volume

        if not isinstance(weight_volume, (int, float)):
            raise TypeError("Вес кита должен быть int или float")
        if weight_volume < 0:
            raise ValueError("Вес кита не может быть отрицательным числом")
        self.weight_volume = weight_volume

    def is_extinction_whale(self) -> bool:
        """
        Функция которая проверяет сколько таких китов

        :return: Количество китов

        Примеры:
        >>> whale = Whale(500, 0)
        >>> whale.is_extinction_whale()
        """
        ...

    def add_year_to_age(self, age: float) -> None:
        """
        Добавление года к возрасту кита.
        :param age: Возраст кита перед добавлением

        :raise ValueError: Если возраст введен не цифрами, то выводится ошибка

        Примеры:
        >>> whale = Whale(500, 0)
        >>> whale.add_year_to_age(200)
        """
        if not isinstance(age, (int, float)):
            raise TypeError("Добавляемый возраст должен быть типа int или float")
        if age < 0:
            raise ValueError("Добавляемый возраст должен быть положительным числом")
        ...

    class Glass:
        def __init__(self, capacity_volume: float, occupied_volume: float):
            """
            Создание и подготовка к работе объекта "Стакан"

            :param capacity_volume: Объем стакана
            :param occupied_volume: Объем занимаемой жидкости

            Примеры:
            >>> glass = Glass(500, 0)  # инициализация экземпляра класса
            """
            if not isinstance(capacity_volume, (int, float)):
                raise TypeError("Объем стакана должен быть типа int или float")
            if capacity_volume <= 0:
                raise ValueError("Объем стакана должен быть положительным числом")
            self.capacity_volume = capacity_volume

            if not isinstance(occupied_volume, (int, float)):
                raise TypeError("Количество жидкости должно быть int или float")
            if occupied_volume < 0:
                raise ValueError("Количество жидкости не может быть отрицательным числом")
            self.occupied_volume = occupied_volume

        def is_empty_glass(self) -> bool:
            """
            Функция которая проверяет является ли стакан пустым

            :return: Является ли стакан пустым

            Примеры:
            >>> glass = Glass(500, 0)
            >>> glass.is_empty_glass()
            """
            ...

        def add_water_to_glass(self, water: float) -> None:
            """
            Добавление воды в стакан.
            :param water: Объем добавляемой жидкости

            :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

            Примеры:
            >>> glass = Glass(500, 0)
            >>> glass.add_water_to_glass(200)
            """
            if not isinstance(water, (int, float)):
                raise TypeError("Добавляемая жидкость должна быть типа int или float")
            if water < 0:
                raise ValueError("Добавляемая жидкость должна положительным числом")
            ...

        def remove_water_from_glass(self, estimate_water: float) -> None:
            """
            Извлечение воды из стакана.

            :param estimate_water: Объем извлекаемой жидкости
            :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
            то возвращается ошибка.

            :return: Объем реально извлеченной жидкости

            Примеры:
            >>> glass = Glass(500, 500)
            >>> glass.remove_water_from_glass(200)
            """
            ...

class Marks:
    def __init__(self, low_volume: float, high_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param low_volume: нижняя граница оценки
        :param high_volume: верхняя граница оценки

        Примеры:
        >>> mark = Marks(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(low_volume, (int, float)):
            raise TypeError("Нижняя граница должна быть типа int или float")
        if low_volume <= 0:
            raise ValueError("Нижняя граница должна быть положительным числом")
        self.low_volume = low_volume

        if not isinstance(high_volume, (int, float)):
            raise TypeError("Верхняя граница должна быть int или float")
        if high_volume < 0:
            raise ValueError("Верхняя граница не может быть отрицательным числом")
        self.high_volume = high_volume

    def is_delete_lowmark(self) -> bool:
        """
        Функция проверяет оценку на совпание с нижней границей

        :return: является ли оценка низкой

        Примеры:
        >>> mark = Marks(2, 5)
        >>> mark.is_delete_lowmark()
        """
        ...

    def add_high_mark(self, rise: float) -> None:
        """
        Добавление балла к оценке.
        :param rise: Количество доп баллов

        :raise ValueError: Если количество доп баллов отрицательное, то вызываем ошибку

        Примеры:
        >>> mark = Marks(2,5)
        >>> mark.add_high_mark(3)
        """
        if not isinstance(rise, (int, float)):
            raise TypeError("Доп баллы должнф быть типа int или float")
        
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
