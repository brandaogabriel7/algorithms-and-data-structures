def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    The list needs to be sorted, if not, the function will return incorrect results
    """

    first = 0
    last = len(list) - 1

    while first <= last:
        middle = (first + last) // 2

        if list[middle] == target:
            return middle
        elif list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in the list")

numbers = [i for i in range(100)]
verify(binary_search(numbers, 5))

numbers = [i for i in range(10, 20)]
verify(binary_search(numbers, 11))

numbers = [i for i in range(1, 2000)]
verify(binary_search(numbers, 1070))

