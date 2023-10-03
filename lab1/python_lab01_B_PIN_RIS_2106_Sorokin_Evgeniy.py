#! /usr/bin/env python
# -*- coding: utf-8 -*-
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации: если на текущей итерации не было обменов, то список уже отсортирован.
        swapped = False
        for j in range(0, n-i-1):
            # Сравниваем соседние элементы и меняем их, если они стоят в неправильном порядке.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если на этой итерации не было обменов, завершаем сортировку.
        if not swapped:
            break

import numpy as np

# Создаем рандомный массив из 10 случайных чисел от -10 до 10
random_array = np.random.randint(-10, 11, 100)

# Укажите путь к файлу, в который вы хотите сохранить массив
file_path = "random_array.txt"

# Сохраняем массив в текстовый файл
np.savetxt(file_path, random_array)

print(f"Рандомный массив сохранен в файл {file_path}")

# Загрузите данные из файла в массив
loaded_array = np.loadtxt(file_path)

# Отсортируйте массив
sorted_array = bubble_sort(loaded_array)

# Укажите путь к файлу, в который вы хотите записать отсортированный массив
sorted_file_path = "sorted_array.txt"

# Запишите отсортированный массив в текстовый файл
np.savetxt(sorted_file_path, sorted_array)

print(f"Отсортированный массив сохранен в файл {sorted_file_path}")