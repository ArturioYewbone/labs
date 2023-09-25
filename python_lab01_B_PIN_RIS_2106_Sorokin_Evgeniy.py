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

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)