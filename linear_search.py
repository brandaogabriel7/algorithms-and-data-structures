def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in the list")

numbers = [i for i in range(10)]

verify(linear_search(numbers, 5))

numbers = [i for i in range(10, 20)]
verify(linear_search(numbers, 11))

numbers = [i for i in range(10, 20)]
verify(linear_search(numbers, 20))
