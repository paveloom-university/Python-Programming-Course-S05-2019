from T1.rectangle import Rectangle # Задание #1
from T2.show_file_info import show_file_info # Задание 2
from T3.sort_rows import sort_rows # Задание 3

# Задание #1
print("\nЗадание #1\n")

## Инициализация объекта
a = Rectangle(14, 5)

## Вывод информации о прямоугольнике
a.info()

## Вычисление и вывод площади прямоугольника
a.area_print()

## Вычисление и вывод периметра прямоугольника
a.per_print()

## Вывод прямоугольника в консоль
a.draw(filled = False)


# Задание #2
print("\n\nЗадание #2\n")

## Вывод информации о файле
show_file_info("./T2/text")


# Задание #3

## Вызов метода для сортировки строк в файле
sort_rows("./T3/in", "./T3/out")


