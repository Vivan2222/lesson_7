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

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
class Water:
    def __init__(self):
        self.content=' Вода '
    def __str__(self):
        return self.content
    def __add__(self, other):
        if other.content=='Воздух':
            return Storm(part1=self, part2=Air())
        if other.content=='Огонь':
            return Steam(part1=self, part2=Fire())
        if other.content=='Земля':
            return Dirt(part1=self, part2=Land())

class Air:
    def __init__(self):
        self.content='Воздух'

    def __add__(self, other):
        if other.content=='Огонь':
            return Lighting(part1=self, part2=Fire())
        if other.content== 'Земля':
            return Dust(part1=self, part2=Land())


    def __str__(self):
        return self.content


class Fire:
    def __init__(self):
        self.content ='Огонь'
    def __str__(self):
        return self.content
    def __add__(self, other):
        if other.content=='Земля':
            return Ejection(part1=self, part2=Land())
class Land:
    def __init__(self):
        self.content='Земля'
    def __str__(self):
        return self.content

class Storm:
    def __init__(self, part1, part2):
        self.part1=part1
        self.part2=part2
        self.content = 'Шторм'
    def __str__(self):
        return ' Я ' + self.content +' состою из ' + str(self.part1) + ' и ' + str(self.part2)
class Steam:
    def __init__(self, part1, part2):
        self.part1=part1
        self.part2=part2
        self.content='Пар'
    def __str__(self):
        return ' Я ' + self.content + ', состою из' + str(self.part1)+ 'и ' + str(self.part2)
class Dirt:
    def __init__(self, part1, part2):
        self.part1=part1
        self.part2=part2
        self.content=' Грязь'
    def __str__(self):
        return 'Я' + self.content + ', состою из' + str(self.part1) + 'и ' + str(self.part2)

class Lighting:
    def __init__(self, part1, part2):
        self.part1=part1
        self.part2=part2
        self.content=' Молния'
    def __str__(self):
        return 'Я' + self.content + ', состою из ' + str(self.part1) + ' и ' + str(self.part2)
class Dust:
    def __init__(self, part1, part2):
        self.part1=part1
        self.part2=part2
        self.content='Пыль'
    def __str__(self):
        return 'Я ' + self.content + ', состою из ' + str(self.part1) + ' и ' + str(self.part2)

class Ejection:
    def __init__(self, part1, part2):
        self.part1=part1
        self.part2=part2
        self.content='Лава'
    def __str__(self):
        return 'Я ' + self.content + ', состою из ' + str(self.part1) + ' и ' + str(self.part2)


# land= Land()
# steam= Steam()
# dirt= Dirt()
# dust=Dust()
# ejection= Ejection()
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
