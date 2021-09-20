"""
Sorting algorithms in python
You can use sorting to solve a wide range of problems:
-searching
-selection
-duplicates
-distrubiton
"""
from random import randint
from timeit import repeat

# build-in sorting algorithm
# array = [8, 2, 6, 4, 2]
# print(sorted(array))


# time complexity
def run_sorting_algorithm(algorithm, array):
    # the coe you run before running the stmt
    # we generally use this to import the required moduels for out code
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"  # statement you want to measure in string

    # Exectue the coe ten different times and return the time
    # number: number of time you want to run your code
    # repeat 3 times and get the mininumal value
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # a common misconception is that you should find the average time of each
    # run. Here we measure the shortest time
    print(f"Algorithm: {algorithm}. Mininum exectuion time: {min(times)}")


# BIG O
# assuming that n is the size of the input to an algorithm,
# the big o notation represents the relationship between n and the number of
# steps the algorithm takes to find a solution.
# O(1) constant
# O(n) linear
# O(n^2) quadratic
# O(2^n) exponential
# O(logn) logarithmic the runngin time grows linearly while the size of the input
# grows exponentially
# O(nlog(n))


# bubble sort
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # create a flag that will allow the function to terminate early
        # if there is nothing left to sort
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array


# big o run time: (n-1) + (n-2) + (n-3) + ... = n(n-1)/2


# insertion_sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item


# merge sort
def merge(left, right):
    # it has a linear runtime O(N)
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # if you reach the end of either array, then you can
        # add the remaining elements from the other array to the result
        # and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    # it has a logarithmic time O(Nlog(N))
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(left=merge_sort(array[:midpoint]),
                 right=merge_sort(array[midpoint:]))


# quick sort
def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)


# quicksort also pays the price of recursion when the list is sufficiently
# small, taking longer to complete than both insertion sort and bubble sort.

# Timsrot algorithm in python
# hibrid sorting algorithm, which employs employs a best-of-both-worlds
# combination of insertion sort and merge sort.
# it is the standard sorting algorithm of the Python language as well as others
# such as Java and Swift


def tim_insertion(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array


def timsort(array):
    min_run = 32
    n = len(array)
    for i in range(0, n, min_run):
        tim_insertion(array, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mindpoint = start + size - 1
            end = min((start + start * 2 - 1), (n - 1))
            merged_array = merge(
                left=array[start:mindpoint + 1],
                right=array[mindpoint + 1:end + 1]
            )
            array[start:start + len(merged_array)] = merged_array

        size *= 2
    return array


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="sorted", array=array)
    # it will take around 3 minutes to run, so be patient
    # run_sorting_algorithm(algorithm="bubble_sort", array=array)
    # >>> Algorithm: bubble_sort. Mininum exectuion time: 92.530373086
    # run_sorting_algorithm(algorithm="insertion_sort", array=array)
    # >>> Algorithm: insertion_sort. Mininum exectuion time: 42.21004641600001
    run_sorting_algorithm(algorithm="merge_sort", array=array)
    run_sorting_algorithm(algorithm="quicksort", array=array)
    run_sorting_algorithm(algorithm="timsort", array=array)
