#!python


def counting_sort(numbers):
    """
    Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) where n is sorted output array, k is range, it takes
    O(n) for iterating the original list(numbers), also building up the output
    list takes O(n), then making counts list takes O(k) as we need to loop
    through range of k.
    Memory usage: O(n+k) , where n is sorted output array, k is range, n for
    output array, k is count list.
    """
    if not numbers:
        return []
    # Find range of given numbers (minimum and maximum integer values)
    start_range = min(numbers)
    end_range = max(numbers)
    # range of given numbers
    n_range = end_range - start_range
    # Create list of counts with a slot for each number in input range
    counts = [0] * (n_range + 1)
    # Loop over given numbers and increment each number's count, it takes O(n)
    for i, num in enumerate(numbers):  # O(n)
        # get the right index to increment
        index = num - start_range
        # increment the count of the number
        counts[index] += 1
        # print(counts)

    # Loop over counts and append that many numbers into output list
    output_list = []
    for i in range(len(counts)):  # O(k)
        for _ in range(counts[i]):
            # redefine the number using the index of counts
            num = i + start_range
            output_list.append(num)
    
    # items = sorted(numbers)
    # print(len(numbers) == len(output_list), items == output_list)
    # FIXME: Improve this to mutate input instead of creating new output list
    numbers[:] = output_list
    return numbers

def bucket_sort(numbers, num_buckets=10):
    """
    Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    """
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


if __name__ == "__main__":
    numbers = [7, 4, 0, 5, 4, 5, 3, 0, 1, 2, 1, 1, 2]
    print(counting_sort(numbers))
