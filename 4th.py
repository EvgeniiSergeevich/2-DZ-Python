# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) 

# -2 -1 0 1 2 
# Позиции: 0,1 -> 2

n = int(input('Введите число: '))
prod = 1


list1 = []
for j in range(-n, n + 1):                               # Заполняю список значениями от -n до n
    list1.append(j)

print(f'Список чисел от -n до n: {list1}')

f = open('file.txt')                    

str2 = ""

for i in f:                                              # Читаю из файла значения для произведения в строку
    str2 += i

l = list(map(int, str2.split('\n')))                     # Делаю список из строки
print(f'Позиции элементов для произведения: {l}')

for i in range(len(l)):                                  # Перемножаю элементы на нужных позициях
    prod *=  int(list1[l[i]])
print(f'Произведение элементов = {prod}')    