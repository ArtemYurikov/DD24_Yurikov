from typing import Union


class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("capacity_volume must be an int or float")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("occupied_volume must be an int or float")
        if capacity_volume <= 0:
            raise ValueError("capacity_volume must be greater than 0")
        if occupied_volume < 0:
            raise ValueError("occupied_volume must be non-negative")
        if occupied_volume > capacity_volume:
            raise ValueError("occupied_volume cannot be greater than capacity_volume")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __str__(self):
        return f"Glass(capacity_volume={self.capacity_volume}, occupied_volume={self.occupied_volume})"


# Реализация объектов Glass
try:
    glass1 = Glass(500, 200)  # корректные значения
    print(glass1)
except (TypeError, ValueError) as e:
    print(e)

try:
    glass2 = Glass(-100, 50)  # некорректное значение для capacity_volume
except (TypeError, ValueError) as e:
    print(e)

try:
    glass3 = Glass(300, 400)  # некорректное значение для occupied_volume
except (TypeError, ValueError) as e:
    print(e)

try:
    glass4 = Glass("500", 200)  # некорректный тип для capacity_volume
except (TypeError, ValueError) as e:
    print(e)

try:
    glass5 = Glass(500, -50)  # некорректное значение для occupied_volume
except (TypeError, ValueError) as e:
    print(e)
