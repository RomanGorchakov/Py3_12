#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import multiprocessing


def calculate_term(x, n, result_queue):
    term = x ** n
    result_queue.put(term)


def calculate_series_sum(x, tolerance):
    result_queue = multiprocessing.Queue()
    processes = []
    n = 0

    while True:
        process = multiprocessing.Process(target=calculate_term, args=(x, n, result_queue))
        processes.append(process)
        process.start()
        process.join()

        term = result_queue.get()
        if abs(term) < tolerance:
            break

        n += 1

    series_sum = 0
    while not result_queue.empty():
        series_sum += result_queue.get()

    return series_sum

if __name__ == "__main__":
    x = 0.7
    tolerance = 1e-6

    series_sum = calculate_series_sum(x, tolerance)
    control_value = 1 / (1 - x)

    print(f"Сумма ряда с точностью {tolerance}: {series_sum}")
    print(f"Контрольное значение функции: {control_value}")
    print(f"Разница: {abs(series_sum - control_value)}")