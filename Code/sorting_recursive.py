#!python
from sorting_iterative import bubble_sort, selection_sort, insertion_sort


def merge(items_1, items_2):
    """
    Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n+m) where n and m are lengths of two sorted lists
    Memory usage: O(n+m) where n and m are lengths of two sorted lists,
    Runnning and memory time is the same for all cases, because we always copy
    all elements from both lists to new merged list.
    Args:
        items_1(list): sorted list of elements
        items_2(list): sorted list of elements
    Returns:
        merged_list(list): merged list of the two sorted lists
    """
    # check if lists are empty
    if not items_1 and not items_2:
        return []

    # used to merge two sorted lists together
    merged_list = []
    index1, index2 = 0, 0

    # iterate until one or both list are done
    while (index1 < len(items_1)) and (index2 < len(items_2)):
        # print(f"i: {index1}, j: {index2}")
        if items_1[index1] <= items_2[index2]:
            merged_list.append(items_1[index1])
            index1 += 1
        else:
            merged_list.append(items_2[index2])
            index2 += 1

    # check if there are still elements in items_1
    if index1 <= len(items_1)-1:
        # copy the rest of the elements from array items_1 to merged_list
        while index1 < len(items_1):
            merged_list.append(items_1[index1])
            index1 += 1

    # check if there are still elements in items_2
    elif index2 <= len(items_2)-1:
        # copy the rest of the elements from array items_2 to merged_list
        while index2 < len(items_2):
            merged_list.append(items_2[index2])
            index2 += 1

    return merged_list


def split_sort_merge(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    where: N = length of the original list, n = length of the first half,
    m = length second half. Also n and m is approximately(almost) equal length.
    so n + m approximately 2n or 2m which is, 2n = N or 2m = N

    Running time: O(n^2) + O(m^2) = O(2n^2) using the properties above, overall
    O(N^2) running time
    Memory usage: O(N), because when we are merging two sorted list at the end
    we are creating new empty list with the same length of the original list.

    Args:
        items(list): unsorted list of elements

    Returns:
        merged_list(list): sorted list of elements of original list. Reference
        of the original list didnt change.
    """
    
    # splitting part
    mid = len(items) // 2
    # copy the first half of the array
    items_1 = items[:mid]  # O(n)
    # copy the second half of the array
    items_2 = items[mid:]  # O(m)

    # sorting the splitted lists using iterative algorithms
    bubble_sort(items_1)  # O(n^2) refer to the bubble sort docstring
    insertion_sort(items_2)  # O(m^2) refer to insertion sort docstring

    # now merge two sorted arrays
    merged_list = merge(items_1, items_2)  # O(n+m) = O(N)
    # items = merged_list.copy()
    return merged_list


def merge_sort(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(nlogn) in all cases, as we need to split the array
    approximately two equal parts in a O(logn) time and merge them back in O(n)
    run time. so overall O(nlogn)
    # TODO: Memory usage: O(nlogn) for recursive stack. Is it for all cases? 
    
    Args:
        items(list): unsorted list of elements
    
    Returns:
        merged_list(list): unsorted list of elements
    """
    # base case if there is only 1 or 0 item in the list return itself
    # since it is already sorted
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    items_1 = merge_sort(items[0:mid])
    items_2 = merge_sort(items[mid:])
    print(f"items_1: {items_1}, items_2: {items_2}")

    return merge(items_1, items_2)


def partition(items, low, high):
    """
    Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing the last element of the list as a pivot and
    from that range, moving pivot into index `p`, items less than pivot into
    range `[low...p-1]`, and items greater than pivot into range `[p+1...high]`

    Best and average case running time: O(logn) when the two halves of the list
    are balanced which means they have apporximately the same length

    Worst case running time: O(n) when one half is much bigger than the other
    half
    
    Memory usage: O(1) always, because we are just swapping elements in-place,
    and using only consant numbe of variables to keep track of the elements.

    Args:
        items(list): unsorted list
        low(int): first index of the list
        high(int): the last element of the list
    
    Returns:
        pivot_index(int): the index of pivot point in the list
    """
    print(f"low: {low}, high {high}")
    
    if high - low >= 2:
        print("items more than 3 element: ", items[low:high])
        print(f"items before median: {items}")
        _find_median(items, low, high)
        print(f"items after: {items}")
        
    
    # last element is the pivot
    pivot = items[high]
    # this is the index where the pivot will be placed after all comparisons
    # made and list is `sorted` relative to the pivot point. or we can see
    # this as the first larger number than the pivot.
    pivot_index = low

    for i in range(low, high):
        if items[i] <= pivot:
            # found the smaller number than the pivot, so swap it with
            # pivot index so it would be left side of the pivot index
            items[i], items[pivot_index] = items[pivot_index], items[i]
            # move the pivot index 1 to the right
            pivot_index += 1
    
    # swap the pivot num from the end to the pivot index
    items[high], items[pivot_index] = items[pivot_index], items[high]
    
    return pivot_index


def quick_sort(items, low=None, high=None):
    """
    Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.

    Best and average case running time: O(nlogn) when two halves of the list
    partitioned approximetely in equal sizes.

    Worst case running time: O(n^2) when two halves of the list partitioned
    lopsided, where one side of the partition is much bigger than the other
    half. In this case we need to repeat the partition `n` times as opposed
    to the average case where the partition happens logn times. This happens
    mostly when list is almost sorted or the pivot point happens to be the
    smallest or the largest number in the list (this rarely happens).

    Best and average case memory usage: O(logn), this is the recursion stack
    paid by the language. Again this depends on how balanced of two halves
    of the list.
    
    Worst case memory usage: O(n)

    Args:
        items(list): unsorted list
        low(int): first index of the list
        high(int): the last element of the list
    """

    if low is None and high is None:
        low = 0
        high = len(items)-1

    if low < high:
        # get the pivot index
        pivot_index = partition(items, low, high)
        # left half of the list to be sorted
        quick_sort(items, low, pivot_index - 1)
        # right half of the list to be sorted
        quick_sort(items, pivot_index + 1, high)


def _find_median(items: list, low=None, high=None):
    """
    Find the median out of 3 numbers and swap the items in the list so median
    will be at the end of the list

    Args:
        items(list): unsorted list
        low(int): 0th index in the list
        high(int): last index in the list
    """
    # set the initial values of low and high
    if low is None and high is None:
        low = 0
        high = len(items) - 1
    
    mid = (high + low) // 2

    if items[mid] < items[low]:
        items[mid], items[low] = items[low], items[mid]
    if items[high] < items[low]:
        items[high], items[low] = items[low], items[high]
    if items[mid] < items[high]:
        items[mid], items[high] = items[high], items[mid]


if __name__ == "__main__":
    splitter = "##############################################################"
    # a = [1, 2, 3, 5, 9, 14]
    # b = [4, 6, 7, 8, 10, 12, 13, 15]
    # merged_list = merge(a, b)
    # print(splitter)
    # print(f"Merging sorted lists: {merged_list}")

    # testing split sort merge function

    # items = [50, 21, 95, 20, 89, 57, 87, 83, 89, 10, 25, 5, 8, 99]
    # split_sort_merged_items = split_sort_merge(items)
    # print(splitter)
    # print(f"Split sort merge: {split_sort_merged_items}")

    # testing merge sort recursively

    # items = [50, 21, 95, 20, 89, 57, 87, 83, 89, 10, 25, 5, 8, 99]
    # merge_sort_rec = merge_sort(items)
    # print(splitter)
    # print(f"Merge sort recursively: {merge_sort_rec}")

    items = [50, 21, 95, 20, 89, 57, 87, 83, 89, 10, 25, 5, 8, 99]
    quick_sort(items)
    print(splitter)
    print(f"Items after quick_sort recursively: {items}")

    # items = [9, 11, 19]
    # median = _find_median(items)
    # print(f"median of {items} is {median}")

