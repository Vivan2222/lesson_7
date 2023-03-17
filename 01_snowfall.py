# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1500, 1200)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:
    def __init__(self):
        self.colour = sd.COLOR_WHITE
        self.length = sd.random_number(5, 20)
        self.item_a = sd.random_number(1, 8) / 10
        self.item_b = sd.random_number(1, 8) / 10
        self.item_c = sd.random_number(30, 60)
        self.x1 = sd.random_number(150, 1500)
        self.y1 = sd.random_number(900, 1000)
        self.speed = sd.random_number(5, 20)
        self.rand = sd.random_number(1, 2)

    def clear_previous_picture(self):
        sd.start_drawing()
        self.colour = sd.background_color
        sd.snowflake(center=sd.get_point(self.x1, self.y1), color=self.colour, factor_a=self.item_a,
                     factor_b=self.item_b, factor_c=self.item_c, length=self.length)
        sd.finish_drawing()

    def move(self):
        rand=sd.random_number(1, 2)
        self.y1 -= self.speed
        if rand==1:
            self.x1+=sd.random_number(1, 5)
        else:
            self.x1-=sd.random_number(1, 5)

    def move_snoflake_colour(self):
        sd.start_drawing()
        self.colour = sd.COLOR_WHITE
        sd.snowflake(center=sd.get_point(self.x1, self.y1), color=self.colour, factor_a=self.item_a,
                     factor_b=self.item_b, factor_c=self.item_c, length=self.length)
        sd.finish_drawing()
def count_snowlfakes(flake, list):
    if flake.y1<250:
        list.remove(flake)
        flake=Snowflake()
        list.append(flake)

N = int(input('Введите число снежинок'))
stock = []
while len(stock) < N:
    flake = Snowflake()
    stock.append(flake)
while True:
    for flake in stock:
        flake.clear_previous_picture()
        flake.move()
        flake.move_snoflake_colour()
        count_snowlfakes(flake, stock)
    if sd.user_want_exit():
        break



# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
# #         break
