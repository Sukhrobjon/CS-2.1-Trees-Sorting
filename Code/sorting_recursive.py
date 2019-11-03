#!python


def merge(items1, items2):
    """
    Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n+m) where n and m are lengths of two sorted lists
    Memory usage: O(n+m) where n and m are lengths of two sorted lists,
    Runnning and memory time is the same for all cases.
    Args:
        items1(list): sorted list of elements
        items2(list): sorted list of elements
    Returns:
        merged_list(list): merged list of the two sorted lists
    """
    # check if lists are empty
    if not items1 and not items2:
        return []

    merged_list = []
    index1, index2 = 0, 0

    # iterate until one or both list are done
    while (index1 < len(items1)) and (index2 < len(items2)):
        # print(f"i: {index1}, j: {index2}")
        if items1[index1] <= items2[index2]:
            merged_list.append(items1[index1])
            index1 += 1
        else:
            merged_list.append(items2[index2])
            index2 += 1

    # check if there are still elements in items1
    if index1 <= len(items1)-1:
        # copy the rest of the elements from array items1 to merged_list
        while index1 < len(items1):
            merged_list.append(items1[index1])
            index1 += 1

    # check if there are still elements in items2
    elif index2 <= len(items2)-1:
        # copy the rest of the elements from array items2 to merged_list
        while index2 < len(items2):
            merged_list.append(items2[index2])
            index2 += 1

    # print(index1, index2)
    return merged_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


if __name__ == "__main__":
    a = [1, 2, 3, 5, 9, 14]
    b = [4, 6, 7, 8, 10, 12, 13, 15]
    merged_list = merge(a, b)
    print(f"Merging sorted lists: {merged_list}")
