# -*- coding: utf-8 -*-
import random

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


from colorama import Fore


class Cat:
    def __init__(self, name):
        self.fully = 30
        self.house = None
        self.name = name

    def sleep(self):
        print(Fore.GREEN + 'Кот {} спит'.format(self.name))
        self.fully -= 10

    def eat(self):
        if self.house.cat_food < 10:
            print(Fore.RED + 'Нет еды для кота')
        else:
            print(Fore.GREEN + '{} поел'.format(self.name))
            self.fully += 20
            self.house.cat_food -= 10

    def tear_wallpaper(self):
        print(Fore.GREEN + '{} дерет обои'.format(self.name))
        self.fully -= 10
        self.house.dirt += 5

    def __str__(self):
        return Fore.CYAN + 'Кот {}, сытость {}'.format(self.name, self.fully)

    def act(self):
        dice = random.randint(1, 2)
        if self.fully <= 10:
            self.eat()
        else:
            if dice == 1:
                self.sleep()
            else:
                self.tear_wallpaper()


class Human:
    def __init__(self, name):
        self.name = name
        self.fully = 10
        self.house = None

    def take_cat(self, cat):
        if self.house is None:
            print(Fore.RED + 'Сначала нужно купить дом а потом можно подобрать кота')
        else:
            print(Fore.GREEN + '{} Подобрал кота {}'.format(self.name, cat.name))
            cat.house = self.house

    def buy_cat_food(self):
        if self.house.money >= 50:
            print(Fore.GREEN + '{} купил еды для кота {}'.format(self.name, cat.name))
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            print(Fore.RED + 'Недостаточно денег для покупки еды коту')

    def clear_house(self):
        print(Fore.GREEN + '{} убрался в доме'.format(self.name))
        self.house.dirt -= 100
        self.fully -= 20

    def eat(self):
        if self.house.food > 9:
            print(Fore.GREEN + '{} поел'.format(self.name))
            self.house.food -= 10
            self.fully += 20
        else:
            print(Fore.RED + 'У {} нет еды'.format(self.name))

    def work(self):
        if self.fully > 9:
            print(Fore.GREEN + '{} пошел на работу'.format(self.name))
            self.fully -= 10
            self.house.money += 150
        else:
            print(Fore.RED + 'Не хватает сил')

    def watch_MTV(self):
        print(Fore.GREEN + '{} смотрел MTV целый день'.format(self.name))
        self.fully -= 10

    def shopping(self):
        if self.house.money > 9:
            print(Fore.GREEN + '{} пошел в магазин'.format(self.name))
            self.house.food += 30
            self.house.money -= 30
        else:
            print(Fore.RED + 'недостаточно денег для покупки еды')

    def into_houes(self, house):
        self.house = house
        self.fully -= 10
        print(Fore.GREEN + '{} вьехал в дом'.format(self.name))

    def __str__(self):
        return Fore.BLUE + 'Я-{}, сытость-{}'.format(
            self.name, self.fully)

    def act(self):
        if self.fully < 10:
            if self.house.food > 10:
                self.eat()
            else:
                if self.house.money > 10:
                    self.shopping()
                else:
                    self.work()
        elif self.house.money < 30:
            self.work()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food < 10:
            if self.house.money > 50:
                self.buy_cat_food()
            else:
                self.work()
        elif self.house.dirt >= 100:
            self.clear_house()
        # elif self.house.food < 10:
        #     self.shopping()
        else:
            self.watch_MTV()


class House:
    def __init__(self):
        self.money = 60
        self.food = 30
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return Fore.BLUE + 'еды осталось-{}, денег осталось-{}, чистота дома {}, еды кота осталось {}'.format(
            self.food, self.money, self.dirt, self.cat_food)


# man = Human('Вася')
# for day in range(365):
#     print(Fore.RESET+'============== день {} =============='.format(day))
#     man.act()
#     print(man)
citizens = [Human('Бивис')]
cats = [Cat('Барсик'), Cat('Байкал'), Cat('Персик')]
my_sweet_home = House()
for citizen in citizens:
    citizen.into_houes(my_sweet_home)
    for cat in cats:
        citizen.take_cat(cat)
for day in range(366):
    print('==========день {}========='.format(day))
    for citizen in citizens:
        citizen.act()
    for cat in cats:
        cat.act()
    print(Fore.RESET + '======в конце дня====')
    for citizen in citizens:
        print(citizen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)




# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
