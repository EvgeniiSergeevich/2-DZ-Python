# Реализуйте алгоритм перемешивания списка.
import random

# a = []                                        # Создание массива из 10 элементов с рандомными числами от 0 до 99
# for i in range(1, 10):
#     a.append(random.randint(0, 100))

a = list(range(10))                             # Создание массива от 0 до 9

print(f'Исходный массив: {a}')
random.shuffle(a)                               # Перемешивание массива
print(f"Перемешанный массив: {a}")