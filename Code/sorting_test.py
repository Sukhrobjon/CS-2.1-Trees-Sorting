#!python

from sorting import random_ints
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort
from sorting_recursive import split_sort_merge, merge_sort, quick_sort
from sorting_integer import counting_sort, bucket_sort
import unittest


class IsSortedTest(unittest.TestCase):
    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([3, 5, 7]) is True
        # new added test cases
        assert is_sorted([3, 7, 9, 11, 13, 15, 16, 17, 19, 20]) is True
        assert is_sorted([1, 2, 4, 5, 7, 8, 10, 15, 25, 25,
                          32, 37, 37, 38, 38, 39, 39, 42, 42, 47]) is True
        assert is_sorted([6, 9, 13, 13, 16, 17, 21, 22, 22,
                          22, 23, 24, 25, 29, 30, 34, 34, 36, 40, 43]) is True

    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        # new test cases
        assert is_sorted([6, 2, 9, 6, 3, 5, 11, 12, 19, 13]) is False
        assert is_sorted([21, 12, 19, 5, 30, 17, 22, 22, 15, 4]) is False
        assert is_sorted([24, 22, 23, 36, 29, 34, 16, 22, 43,
                          9, 13, 22, 6, 34, 40, 30, 25, 17, 21, 13]) is False

    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        # new test cases
        assert is_sorted(['A', 'C', 'E', 'K', 'L', 'N', 'P', 'S', 'U', 'X']) is True
        assert is_sorted(['B', 'E', 'K', 'L', 'M', 'O', 'P', 'S', 'U', 'Z']) is True
        assert is_sorted(['B', 'D', 'E', 'F', 'L', 'M', 'O', 'S', 'T', 'W']) is True

    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        # extra test cases added
        assert is_sorted(['A', 'K', 'P', 'N', 'U', 'X', 'C', 'S', 'E', 'L']) is False
        assert is_sorted(['B', 'K', 'P', 'M', 'U', 'Z', 'L', 'S', 'E', 'O']) is False
        assert is_sorted(['D', 'F', 'B', 'M', 'E', 'W', 'L', 'S', 'T', 'O']) is False

    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted
    
    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted


class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert(bubble_sort([])) == []  # Empty lists are vacuously sorted
        assert bubble_sort([3]) == [3]  # Single item is trivially sorted
        assert bubble_sort([3, 3]) == [3, 3]  # Duplicate items are in order
        assert bubble_sort([3, 5]) == [3, 5]
        assert bubble_sort([3, 5, 7]) == [3, 5, 7]
        # new added test cases
        sample_1 = [3, 7, 9, 11, 13, 15, 16, 17, 19, 20]
        assert bubble_sort(sample_1) == sample_1
        sample_2 = [1, 2, 4, 5, 7, 8, 10, 15, 25, 25, 32,
                    37, 37, 38, 38, 39, 39, 42, 42, 47]
        assert bubble_sort(sample_2) == sample_2
        sample_3 = [6, 9, 13, 13, 16, 17, 21, 22, 22,
                    22, 23, 24, 25, 29, 30, 34, 34, 36, 40, 43]
        assert bubble_sort(sample_3) == sample_3

    def test_bubble_sort_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        sample_1 = [5, 3]
        assert bubble_sort(sample_1) == sorted(sample_1)
        sample_2 = [3, 5, 3]
        assert bubble_sort(sample_2) == sorted(sample_2)
        sample_3 = [7, 5, 3]
        assert bubble_sort(sample_3) == sorted(sample_3)
        sample_4 = [37, 3, 5, 6, 41, 50, 17, 5, 18, 17]
        # new test cases
        assert bubble_sort(sample_4) == sorted(sample_4)
        sample_5 = [21, 12, 19, 5, 30, 17, 22, 22, 15, 4]
        assert bubble_sort(sample_5) == sorted(sample_5)
        sample_6 = [21, 23, 19, 16, 31, 27, 18, 6, 43, 41, 43, 12, 32, 38, 35]
        assert bubble_sort(sample_6) == sorted(sample_6)


class SelectionSortTest(unittest.TestCase):
    def test_selection_sort_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert selection_sort([]) == []  # Empty lists are vacuously sorted
        assert selection_sort([3]) == [3]  # Single item is trivially sorted
        assert selection_sort([3, 3]) == [3, 3]  # Duplicate items are in order
        assert selection_sort([3, 5]) == [3, 5]
        assert selection_sort([3, 5, 7]) == [3, 5, 7]
        # new added test cases
        sample_1 = [3, 7, 9, 11, 13, 15, 16, 17, 19, 20]
        assert selection_sort(sample_1) == sample_1
        sample_2 = [1, 2, 4, 5, 7, 8, 10, 15, 25, 25, 32,
                    37, 37, 38, 38, 39, 39, 42, 42, 47]
        assert selection_sort(sample_2) == sample_2
        sample_3 = [6, 9, 13, 13, 16, 17, 21, 22, 22,
                    22, 23, 24, 25, 29, 30, 34, 34, 36, 40, 43]
        assert selection_sort(sample_3) == sample_3

    def test_selection_sort_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        sample_1 = [5, 3]
        assert selection_sort(sample_1) == sorted(sample_1)
        sample_2 = [3, 5, 3]
        assert selection_sort(sample_2) == sorted(sample_2)
        sample_3 = [7, 5, 3]
        assert selection_sort(sample_3) == sorted(sample_3)
        sample_4 = [37, 3, 5, 6, 41, 50, 17, 5, 18, 17]
        # new test cases
        assert selection_sort(sample_4) == sorted(sample_4)
        sample_5 = [21, 12, 19, 5, 30, 17, 22, 22, 15, 4]
        assert selection_sort(sample_5) == sorted(sample_5)
        sample_6 = [21, 23, 19, 16, 31, 27, 18, 6, 43, 41, 43, 12, 32, 38, 35]
        assert selection_sort(sample_6) == sorted(sample_6)


class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert insertion_sort([]) == []  # Empty lists are vacuously sorted
        assert insertion_sort([3]) == [3]  # Single item is trivially sorted
        assert insertion_sort([3, 3]) == [3, 3]  # Duplicate items are in order
        assert insertion_sort([3, 5]) == [3, 5]
        assert insertion_sort([3, 5, 7]) == [3, 5, 7]
        # new added test cases
        sample_1 = [3, 7, 9, 11, 13, 15, 16, 17, 19, 20]
        assert insertion_sort(sample_1) == sample_1
        sample_2 = [1, 2, 4, 5, 7, 8, 10, 15, 25, 25, 32,
                    37, 37, 38, 38, 39, 39, 42, 42, 47]
        assert insertion_sort(sample_2) == sample_2
        sample_3 = [6, 9, 13, 13, 16, 17, 21, 22, 22,
                    22, 23, 24, 25, 29, 30, 34, 34, 36, 40, 43]
        assert insertion_sort(sample_3) == sample_3

    def test_insertion_sort_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        sample_1 = [5, 3]
        assert insertion_sort(sample_1) == sorted(sample_1)
        sample_2 = [3, 5, 3]
        assert insertion_sort(sample_2) == sorted(sample_2)
        sample_3 = [7, 5, 3]
        assert insertion_sort(sample_3) == sorted(sample_3)
        sample_4 = [37, 3, 5, 6, 41, 50, 17, 5, 18, 17]
        # new test cases
        assert insertion_sort(sample_4) == sorted(sample_4)
        sample_5 = [21, 12, 19, 5, 30, 17, 22, 22, 15, 4]
        assert insertion_sort(sample_5) == sorted(sample_5)
        sample_6 = [21, 23, 19, 16, 31, 27, 18, 6, 43, 41, 43, 12, 32, 38, 35]
        assert insertion_sort(sample_6) == sorted(sample_6)


class IntegerSortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        sort(items3)
        assert items3 == [3, 5, 7]
        # TODO: Write more test cases with assert equal list statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # ...

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        sort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        sort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        sort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        sort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
        # TODO: Create lists of integers with many duplicate values
        # TODO: Write more test cases with assert equal list statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # ...

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = random_ints(10, 1, 20)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = random_ints(20, 1, 50)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = random_ints(30, 1, 100)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = random_ints(20, 1, 10)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = random_ints(50, 1, 20)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = random_ints(100, 1, 30)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3


class StringSortTest(unittest.TestCase):

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        sort(items3)
        assert items3 == ['A', 'B', 'C']
        # TODO: Write more test cases with assert equal list statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # ...

    def test_sort_on_fish_book_title(self):
        items = 'one fish two fish red fish blue fish'.split()
        sorted_items = sorted(items)  # Create a copy of list in sorted order
        sort(items)  # Call mutative sort function to sort list items in place
        assert items == sorted_items

    def test_sort_on_seven_dwarf_names(self):
        items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items


def get_sort_function():
    """Read command-line argument and return sort function with that name."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort_function'.format(script))
        print('Example: {} bubble_sort'.format(script))
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
            return sort_function
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if 'sort' in name:
                    print('    {}'.format(name))
            return


# If using PyTest, change this variable to the sort function you want to test
sort = split_sort_merge


if __name__ == '__main__':
    # Get sort function from command-line argument
    # FIXME: This is causing unittest to throw an error
    # sort = get_sort_function()
    unittest.main()
