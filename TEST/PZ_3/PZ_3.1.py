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

if(x > 0 and y > 0):
    print("True")
elif(x < 0 and y < 0):
    print("True")
else:
    print("False")
