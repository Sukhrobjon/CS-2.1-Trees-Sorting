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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


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
    print(f"# of swaps: {swaps}")
    return items


def insertion_sort(items):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
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
    print(f"# of swaps: {swaps}")
    return items


def insertion_sort_thom(items):
    """
        Sort given items by taking first unsorted item, inserting it in sorted
        order in front of items, and repeating until all items are in order.
        Args:
            list of ints.
        Output:
            list of ints in ascending order.
    """
    swaps = 0
    for i in range(1, len(items)):
        # set current value to index i (1)
        current_val = items[i]
        # while previous element is *not* in sorted order & index is > 0
        # i will represent the range of the "sorted" section of the list
        while items[i-1] > current_val and i > 0:
            # set current value to previous value
            items[i] = items[i-1]
            # decrement index
            i = i-1
            
        # if current_val was not in sorted order, it will get replaced because
        # i was decremented. If not, loop continues.
        items[i] = current_val
        swaps += 1
    print(f"thoms swaps: {swaps}")
    return items


if __name__ == "__main__":
    sorted_items = [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]
    unsorted_items = [3, 15, 4, 7, 20, 6, 18, 9, 7]
    sample = [3, 1, 5, 2, 18, 14]
    # rand_nums = [random.randint(1, 100) for i in range(20)]
    # print(rand_nums)
    rand_nums = [15, 28, 18, 81, 39, 50, 15, 16, 78,
                 14, 69, 22, 89, 41, 97, 59, 78, 40, 62, 32]
    print(rand_nums)
    insertion_sort = insertion_sort(unsorted_items)
    thom_insertion_sort = insertion_sort_thom(unsorted_items)
    
    print(f"insertion sort result: {insertion_sort}")
    print(f"Thom's insertion sort result: {thom_insertion_sort}")
