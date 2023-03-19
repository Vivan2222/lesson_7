# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
#   Камень + Вода = Песок
#   Камень + Огонь = Металл
#   Камень + земля = Нефть

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
class Water:
    def __str__(self):
        return 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Land):
            return Dirt()

class Air:
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lighting()
        elif isinstance(other, Land):
            return Dust()


class Fire:
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other, Land):
            return Ejection()

class Land:
    def __str__(self):
        return 'Земля'

class Stone:
    def __str__(self):
        return 'Камень'
    def __add__(self, other):
        if isinstance(other, Water):
            return Sand()
        elif isinstance(other, Air):
            return Fire()
        elif isinstance(other, Fire):
            return Metal()
        elif isinstance(other, Land):
            return Oil()

class Oil:
    def __str__(self):
        return 'Нефть'
class Metal:
    def __str__(self):
        return 'Металл'
class Sand:
    def __str__(self):
        return 'Песок'
class Storm:
    def __str__(self):
        return 'Шторм'
class Steam:
    def __str__(self):
        return 'Пар'
class Dirt:
    def __str__(self):
        return 'Грязь'

class Lighting:
    def __str__(self):
        return 'Молния'
class Dust:
    def __str__(self):
        return 'Пыль'

class Ejection:

    def __str__(self):
        return 'Лава'
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Land(), '=', Water() + Land())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Land(), '=', Air() + Land())
print(Fire(), '+', Land(), '=', Fire() + Land())
print(Stone(), '+', Water(), '=', Stone() + Water())
print(Stone(), '+', Air(), '=', Stone() + Air())
print(Stone(), '+', Fire(), '=', Stone() + Fire())
print(Stone(), '+', Land(), '=', Stone() + Land())



# land= Land()
# steam= Steam()
# dirt= Dirt()
# dust=Dust()
# ejection= Ejection()
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
