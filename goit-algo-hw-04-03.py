import timeit

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from quicksort import quicksort
from merge_sort import merge_sort
from radix_sort import counting_sort

import random

if __name__ == "__main__":
    # Генерація випадкового списку чисел
    random_list = [random.randint(1, 10000) for _ in range(10000)]

    # Вимірювання часу виконання для кожного алгоритму сортування
    print(
        "Bubble Sort Time:",
        timeit.timeit(lambda: bubble_sort(random_list[:]), number=10),
    )
    print(
        "Insertion Sort Time:",
        timeit.timeit(lambda: insertion_sort(random_list[:]), number=10),
    )
    print(
        "Selection Sort Time:",
        timeit.timeit(lambda: selection_sort(random_list[:]), number=10),
    )
    print(
        "Shell Sort Time:", timeit.timeit(lambda: shell_sort(random_list[:]), number=10)
    )
    print(
        "Quicksort Time:", timeit.timeit(lambda: quicksort(random_list[:]), number=10)
    )
    print(
        "Merge Sort Time:", timeit.timeit(lambda: merge_sort(random_list[:]), number=10)
    )
    print(
        "Radix Sort Time:",
        timeit.timeit(lambda: counting_sort(random_list[:], 1), number=10),
    )
