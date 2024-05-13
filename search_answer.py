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
    while min_index <= max_index:
        # cut the range in half
        current_index = (min_index + max_index) // 2

        # if the target is right in the middle, just return the index!
        if target_value == values[current_index]:
            return current_index
        # if the target is "above" the midpoint, move the min_index up
        # "+1" because we already know it's not directly equal to midpoint
        elif target_value > values[current_index]:
            min_index = current_index + 1
        # if the target is "below" the midpoint, move the max_index down
        # "-1" because we already know it's not directly equal to midpoint
        else:
            max_index = current_index - 1

    return -1


def binary_search_recursive(values: list, target_value: int) -> int:
    """Wrapper function to encapsulate the initial conditions for recursive
    binary search"""
    return binary_search_recursive_helper(values, target_value, 0, len(values) - 1, 0)

def binary_search_recursive_helper(values: list, target_value: int, min_index: int, max_index: int) -> int:
    """Returns the index of value `target_value` in the list `values`. NOTE:
    `values` MUST be sorted! This is basically the same logic as the iterative
    version. We also have two initial conditions: min_index and max_index."""
    # cut the range in half
    current_index = (min_index + max_index) // 2

    # BASE CASE 1
    # reached the end and didn't find it
    if min_index > max_index:
        return -1
    # BASE CASE 2
    # if the target is right in the middle, just return the index!
    elif target_value == values[current_index]:
        return current_index
    # RECURSIVE OPTION 1
    # if the target is "above" the midpoint, move the min_index up
    # "+1" because we already know it's not directly equal to midpoint
    elif target_value > values[current_index]:
        return binary_search_recursive_helper(values, target_value, current_index + 1, max_index)
    # RECURSIVE OPTION 2
    # if the target is "below" the midpoint, move the max_index down
    # "-1" because we already know it's not directly equal to midpoint
    else:
        return binary_search_recursive_helper(values, target_value, min_index, current_index - 1)



def main():
    # test with numbers
    values = [1, 5, 13, 17, 23, 31, 38, 42, 45, 50]
    print('list:', values)

    print('should find every item and output indices sequentially, plus 3 items not in the list.')
    for target_value in values + [51, 99, 121]:
        # found_index = linear_search(values, target_value)
        found_index = binary_search(values, target_value)
        # found_index = binary_search_recursive(values, target_value)

        if found_index >= 0:
            print(f'found {target_value}: index =', found_index)
        else:
            print(f'not found {target_value}')


    # test with strings
    values = ['apple', 'banana', 'grapefruit', 'pear', 'starfruit']
    print('list:', values)

    print('should find every item and output indices sequentially, plus 3 items not in the list.')
    for target_value in values + ['tomato', 'canteloupe', 'strawberry']:
        # found_index = linear_search(values, target_value)
        found_index = binary_search(values, target_value)
        # found_index = binary_search_recursive(values, target_value)

        if found_index >= 0:
            print(f'found {target_value}: index =', found_index)
        else:
            print(f'not found {target_value}')


if __name__ == '__main__':
    main()