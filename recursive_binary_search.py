def recursive_binary_search(list, target):
    """
    Returns True if the target is found in the list, else returns False
    The list needs to be sorted, if not, the function will return incorrect results
    """

    if len(list) == 0:
        return False
    else:
        middle = len(list) // 2

        if list[middle] == target:
            return True

        if list[middle] < target:
            return recursive_binary_search(list[middle + 1:], target)
        
        return recursive_binary_search(list[:middle], target)
    
def verify(result):
    print(f"Target found: {result}")

numbers = [i for i in range(100)]
verify(recursive_binary_search(numbers, 5))

numbers = [i for i in range(10, 20)]
verify(recursive_binary_search(numbers, 21))

numbers = [i for i in range(1, 2000)]
verify(recursive_binary_search(numbers, 1070))

