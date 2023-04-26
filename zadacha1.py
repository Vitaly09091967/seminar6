# Задача 30:  Заполните массив элементами арифметической прогрессии. Её 
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

arr = [a1 + (i * d) for i in range(n)]
print("Элементы прогрессии: ", arr)