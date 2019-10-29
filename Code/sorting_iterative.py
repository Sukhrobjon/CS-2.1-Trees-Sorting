#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    for i in range(len(items)):
        # last sorted elements index in the array
        min_idx = i
        # rest of right side of the unsorted array
        for j in range(i+1, len(items)):
            if items[j] < items[i]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items



if __name__ == "__main__":
    items = [1, 2, 3, 4]
    un_items = [3, 2, 6, 5]
    print(selection_sort(un_items))
