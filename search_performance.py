'''Separate file for performance testing on linear and binary search. Binary
search is implemented differently here to add "iterations" in the return
value.'''
import time

def linear_search(values: list, target_value: int) -> int:
    """Returns the index of value `target_value` in the list `values`"""
    for i in range(len(values)):
        # if the target is found, return the index that it's found at
        if values[i] == target_value:
            return i

    # otherwise, return -1 (convention meaning "this target value wasn't found")
    return -1


def binary_search(values: list, target_value: int) -> int:
    """Returns the index of value `target_value` in the list `values`. NOTE:
    `values` MUST be sorted!"""

    min_index = 0
    max_index = len(values) - 1
    iterations = 0 # for performance analysis only
    while min_index <= max_index:
        iterations += 1
        # cut the range in half
        current_index = (min_index + max_index) // 2

        # if the target is right in the middle, just return the index!
        if target_value == values[current_index]:
            return current_index, iterations
        # if the target is "above" the midpoint, move the min_index up
        # "+1" because we already know it's not directly equal to midpoint
        elif target_value > values[current_index]:
            min_index = current_index + 1
        # if the target is "below" the midpoint, move the max_index down
        # "-1" because we already know it's not directly equal to midpoint
        else:
            max_index = current_index - 1

    return -1, iterations


def binary_search_recursive(values: list, target_value: int) -> int:
    """Wrapper function to encapsulate the initial conditions for recursive
    binary search"""
    return binary_search_recursive_helper(values, target_value, 0, len(values) - 1, 0)

def binary_search_recursive_helper(values: list, target_value: int, min_index: int, max_index: int, iterations: int) -> int:
    """Returns the index of value `target_value` in the list `values`. NOTE:
    `values` MUST be sorted! This is basically the same logic as the iterative
    version. We also have two initial conditions: min_index and max_index."""
    iterations += 1 # for performance analysis only

    # cut the range in half
    current_index = (min_index + max_index) // 2

    # BASE CASE 1
    # reached the end and didn't find it
    if min_index > max_index:
        return -1, iterations
    # BASE CASE 2
    # if the target is right in the middle, just return the index!
    elif target_value == values[current_index]:
        return current_index, iterations
    # RECURSIVE OPTION 1
    # if the target is "above" the midpoint, move the min_index up
    # "+1" because we already know it's not directly equal to midpoint
    elif target_value > values[current_index]:
        return binary_search_recursive_helper(values, target_value, current_index + 1, max_index, iterations)
    # RECURSIVE OPTION 2
    # if the target is "below" the midpoint, move the max_index down
    # "-1" because we already know it's not directly equal to midpoint
    else:
        return binary_search_recursive_helper(values, target_value, min_index, current_index - 1, iterations)


def test_performance():
    # generate a bunch of sequential numbers
    how_many = 10_000
    values = []
    for n in range(how_many):
        values.append(n)

    # test algorithms for worst case
    start_time = time.time_ns()
    num_iterations = []
    for n in range(how_many):
        found_index = linear_search(values, n)
        # iterations just equals index of found element
        num_iterations.append(found_index + 1)
    end_time = time.time_ns()
    print(f'linear search: max {max(num_iterations)} iterations\t\t {(end_time - start_time) / 10**9} sec')

    num_iterations.clear()
    start_time = time.time_ns()
    for n in range(how_many):
        found_index, iterations = binary_search(values, n)
        num_iterations.append(iterations)
    end_time = time.time_ns()
    print(f'binary search: max {max(num_iterations)} iterations\t\t {(end_time - start_time) / 10**9} sec')

    num_iterations.clear()
    start_time = time.time_ns()
    for n in range(how_many):
        found_index, iterations = binary_search_recursive(values, n)
        num_iterations.append(iterations)
    end_time = time.time_ns()
    print(f'binary search (recursive): max {max(num_iterations)} iterations\t {(end_time - start_time) / 10**9} sec')


if __name__ == '__main__':
    test_performance()