import time

def linear_search(values: list, target_value: int) -> int:
    """Returns the index of value `target_value` in the list `values`"""
    # otherwise, return -1 (convention meaning "this target value wasn't found")
    return -1


def binary_search(values: list, target_value: int) -> int:
    """Returns the index of value `target_value` in the list `values`. NOTE:
    `values` MUST be sorted!"""
    return -1


def binary_search_recursive(values: list, target_value: int) -> int:
    """Wrapper function to encapsulate the initial conditions for recursive
    binary search"""
    return binary_search_recursive_helper(values, target_value, 0, len(values) - 1, 0)

def binary_search_recursive_helper(values: list, target_value: int, min_index: int, max_index: int) -> int:
    """Returns the index of value `target_value` in the list `values`. NOTE:
    `values` MUST be sorted! This is basically the same logic as the iterative
    version. We also have two initial conditions: min_index and max_index."""
    return -1


def main():
    # generate some raw data
    values = [1, 5, 13, 17, 23, 31, 38, 42, 45, 50]

    print('list:', values)
    print('should find every number and output indices sequentially, plus 3 numbers not in the list.')
    for target_value in values + [51, 99, 121]:
        found_index = linear_search(values, target_value)
        # found_index = binary_search(values, target_value)
        # found_index = binary_search_recursive(values, target_value)

        if found_index >= 0:
            print(f'found {target_value}: index =', found_index)
        else:
            print(f'not found {target_value}')


if __name__ == '__main__':
    main()