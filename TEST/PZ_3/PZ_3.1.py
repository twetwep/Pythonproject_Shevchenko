#Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у) лежит в первой или третьей координатной четверти»

x = input("Введите координату x: ")
while type(x)!= float:
    try:
        x = float(x)
    except ValueError:
        print("Введена неправильная координата: ")
        x = input("Введите координату x: ")

y = input("Введите координату y: ")
while type(y) != float:
    try:
        y = float(y)
    except ValueError:
        print ("Введена неправильная координата: ")
        y = input("Введите координату y: ")

first_third = (x > 0 and y > 0) or (x < 0 and y < 0)

print("Точка лежит в первой или третьей четверти: ", first_third)