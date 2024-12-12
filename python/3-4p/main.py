# print('Команда выводит на экран')
# """
# Много
# Строчный
# Коментарий
# """
# print('Тут можно написать любой текст')
# print('\nПеред этой строкой две пустые строки')
# ("Табуляция\t это \t\t 4 \t пробела")
# print("\\n - новая строка")
# print("\\t - табуляция 4 пробела")
# print("\"\" ")
# print("'' ")
# print("Команда end", end="!\n" )
# print("Команда", "sep", "ставит", "знак", "между", "словами", sep="-")
#
#


"""
Переменная - ячейка памяти которая хранит данные
Типы данных - характеристика значений, которые хранятся в ячейки памяти
"""

#считает периметр площадь и диаганаль квадрата
# def square1 (side):
#    p = side*4
#    s = side*side
#    diag = (side**2+side**2)**0.5
#    return p, s, diag
# print(square1(int(input("Введите сторону квадрата: "))))
# #создание строковой переменной
# string1 = "Hello"
# #вывод строковой переменной
# print(string1)
# #создание числовой переменной
# number1= 8
# #вывод числовой  переменной
# print(number1)
# string2 = input("введите слово: ")
# print("Введеное солово: ", string2)
# string3 = input("введите слово: ")
# print(f"Введеное солово:  {string3}")
# print(string2 + string3) # склеивание стро(конкантенация)
# print(string2 + " " + string3)
#
# number2 = int(input("введите число 1 : "))
# number3 = int(input("введите число 2 : "))
# #сложил и сохранил результат в переменную
# res = number2+number3
# print(res)
# print(" (\\(\\    (\\ /)  (\\ /) \n (-.-)   (. .)  (^_^) \n o_(\")(\")(\")(\") (___)o", end="\n")
# print("          ___     ___ \n         /   \\~~~/   \\ \n  ,----(      . .     )\n /      \\____    ___/\n/|          (\\   |(\n^\\    /___\\  /\\  |\n  |__|    |__| -\"\n")
# print("../\\,,./\\. \n.(='•'= ).\n.(\"),,.(\").\n.\\,\\,,,/,/\n.|,,,. ,,|\n./,,/,,\\,,\\\n.(,,)\"| |\"(,,)\n. ...((...\n. .. .))...\n. ...((...")
import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Lighting Demo"
MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

   def __init__(self, width, height, title):
       super().__init__(width, height, title, resizable=True)

       self.background_sprite_list = None
       self.player_list = None
       self.wall_list = None
       self.player_sprite = None

       self.physics_engine = None

   def setup(self):
       self.background_sprite_list = arcade.SpriteList()
       self.player_list = arcade.SpriteList()
       self.wall_list = arcade.SpriteList()

       self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                          0.4)
       self.player_sprite.center_x = 64
       self.player_sprite.center_y = 270
       self.player_list.append(self.player_sprite)

       for x in range(-128, 2000, 128):
           for y in range(-128, 1000, 128):
               sprite = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png")
               sprite.position = x, y
               self.background_sprite_list.append(sprite)

       self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

   def on_draw(self):
       self.clear()
       self.background_sprite_list.draw()
       self.player_list.draw()

   def on_key_press(self, key, _):
       if key == arcade.key.UP:
           self.player_sprite.change_y = MOVEMENT_SPEED
       elif key == arcade.key.DOWN:
           self.player_sprite.change_y = -MOVEMENT_SPEED
       elif key == arcade.key.LEFT:
           self.player_sprite.change_x = -MOVEMENT_SPEED
       elif key == arcade.key.RIGHT:
           self.player_sprite.change_x = MOVEMENT_SPEED

   def on_key_release(self, key, _):
       if key == arcade.key.UP or key == arcade.key.DOWN:
           self.player_sprite.change_y = 0
       elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
           self.player_sprite.change_x = 0

   def on_update(self, delta_time):
       self.physics_engine.update()


if __name__ == "__main__":
   window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   window.setup()
   arcade.run()