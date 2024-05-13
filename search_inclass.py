def linear_search(values: list, target_value: int) -> int:
    """Returns the index of value `target_value` in the list `values`"""
    # check one item at a time
    # see if item matches target
    # repeat until we find the item or we've gone through the whole list
    return -1


def binary_search(values: list, target_value: int) -> int:
    """Returns the index of value `target_value` in the list `values`. NOTE:
    `values` MUST be sorted!"""
    # initialize LO and HI
    # while LO <= HI (haven't passed each other)
    #   MID = halfway between LO and HI
    #   if target_value = values[MID]: return MID
    #   elif target_value > values[MID]: LO = MID + 1 (chop off LO half)
    #   else: HI = MID - 1 (chop off HI half)
    return -1


def binary_search_recursive(values: list, target_value: int) -> int:
    """Wrapper function to encapsulate the initial conditions for recursive
    binary search"""
    return binary_search_recursive_helper(values, target_value, 0, len(values) - 1, 0)

def binary_search_recursive_helper(values: list, target_value: int, lo_index: int, hi_index: int) -> int:
    """Returns the index of value `target_value` in the list `values`. NOTE:
    `values` MUST be sorted! This is basically the same logic as the iterative
    version. We also have two initial conditions: min_index and max_index."""
    # MID = halfway between LO and HI
    # Base Case 1: if LO > HI: return -1 (LO and HI have passed each other)
    # Base Case 2: if target_value = values[MID]: return MID
    # Recursive Step 1: elif target_value > values[MID]: LO = MID + 1 (chop off LO half)
    # Recursive Step 2: else: HI = MID - 1 (chop off HI half)
    return -1


def main():
    # generate some raw data
    values = [1, 5, 13, 17, 23, 31, 38, 42, 45, 50]

    print('list:', values)
    print('should find every number and output indices sequentially, plus 3 numbers not in the list.')

    for target_value in values + [51, 99, 121]:
        # TODO: call functions to test
        found_index = -1

        if found_index >= 0:
            print(f'found {target_value}: index =', found_index)
        else:
            print(f'not found {target_value}')


if __name__ == '__main__':
    main()