#!python
import random


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n), because iterating through the list once
    TODO: Memory usage: O(1) we are not creating extra space"""
    # TODO: Check that all adjacent items are in order, return early if so

    i = 0
    j = 1

    while j <= len(items) - 1:
        if items[i] > items[j]:  # found unsorted pair
            return False
        i += 1
        j += 1

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: Worst case and Average -> O(n^2),
    Best case O(n) is when the list is already sorted.
    Memory usage: O(1) We are using only couple of variables"""
    swaps = -1
    total_swaps = 0
    while swaps != 0:
        swaps = 0
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swaps += 1
                total_swaps += 1
    print(f"bubble sort swaps: {total_swaps}")
    return items


def selection_sort(items):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: Best, average and worst time is O(n^2)
    Memory usage: O(1) It is allocated memory for variables. we are not
    using any data structure in the memory.
    NOTE: This is the worst sorting algorithm. Use Insertion instead.
    Args:
        items(list): list of unsorted elements
    Return:
        items(list): sorted list inplace
    """
    swaps = 0
    for i in range(len(items)):
        # last sorted elements index in the array
        min_idx = i
        # rest of right side of the unsorted array
        for j in range(i+1, len(items)):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
        swaps += 1
    print(f"Selection sort swaps: {swaps}")
    return items


def insertion_sort(items):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Worst case and Average -> O(n^2),
    Best case O(n) is when the list is already sorted.
    Memory usage: O(1) We are using only couple of variables
    Args:
        items(list): list of unsorted elements
    Return:
        items(list): inplace sorted list
    """
    swaps = 0
    for i in range(1, len(items)):
        # first unsorted item on the right side of the last sorted item
        for j in range(i-1, -1, -1):
            # if the unsorted item is less the sorted element in the list
            # swap their position
            # print(f"j+1: {items[j+1]}, j: {items[j]}")
            # print(f"j: {j}")
            if items[j] > items[j+1]:
                # print(f"items before swap: {items}")
                items[j], items[j+1] = items[j+1], items[j]
                swaps += 1
                # print(f"items after swap: {items}")
            # found the right spot for the unsorted item in the sorted part
            # of the list
            else:
                # print("break it")
                break
    print(f"Insertion sort swaps: {swaps}")
    return items


# to bubble sort
if __name__ == "__main__":
    sorted_items = [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]
    unsorted_items = [3, 15, 4, 7, 20, 6, 18, 9, 7]
    sample = [6, 2, 4, 3]
    # rand_nums = [random.randint(1, 100) for i in range(10)]
    
    rand_nums = [50, 21, 95, 20, 89, 57, 87, 83, 89, 10]
    print(rand_nums)
    bubble_sort = bubble_sort(rand_nums)
    print(f"Bubble sort: {bubble_sort}")
    
    rand_nums = [50, 21, 95, 20, 89, 57, 87, 83, 89, 10]
    selection_sort = selection_sort(rand_nums)
    print(f"Selection sort result: {selection_sort}")

    rand_nums = [50, 21, 95, 20, 89, 57, 87, 83, 89, 10]
    insertion_sort = insertion_sort(rand_nums)
    print(f"Insertion sort result: {insertion_sort}")
