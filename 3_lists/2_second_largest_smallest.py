from typing import List


def second_largest(lst: List[int]) -> int:
    lst.sort()  # O(nlogn)

    second_largest = lst[-2]

    for i in range(len(lst) - 2, 0, -1):  # O(n)
        if lst[i] != lst[-1]:
            second_largest = lst[i]
            break

    return second_largest


def second_smallest(lst: List[int]) -> int:
    lst.sort()

    second_smallest = lst[1]

    for i in range(1, len(lst)):
        if lst[i] != lst[0]:
            second_smallest = lst[i]
            break

    return second_smallest


def second_largest_v2(lst: List[int]) -> int:
    """
    This function finds the second largest number in a given list.

    Parameters:
    lst (List[int]): The input list of integers.

    Returns:
    int: The second largest number in the list.

    Note:
    This function assumes that the list contains at least two unique integers.
    """

    # Initialize the largest number as the first element of the list
    largest = lst[0]

    # Iterate over the list to find the largest number
    for i in lst:  # O(n)
        if i > largest:
            largest = i

    # Initialize the second largest number as negative infinity
    second_largest = float('-inf')

    # Iterate over the list to find the second largest number
    for i in lst:  # O(n)
        if i > second_largest and i != largest:
            second_largest = i

    return second_largest


def second_smallest_v2(lst: List[int]) -> int:
    smallest = lst[0]

    for i in lst:  # O(n)
        if i < smallest:
            smallest = i

    second_smallest_number = float('inf')

    for i in lst:  # O(n)
        if second_smallest_number > i > smallest:
            second_smallest_number = i

    return second_smallest_number


def second_largest_v3(lst: List[int]) -> int:
    """
    This function finds the second largest number in a given list.

    Parameters:
    lst (List[int]): The input list of integers.

    Returns:
    int: The second largest number in the list.

    Note:
    This function assumes that the list contains at least two unique integers.
    """
    # Initialize the largest number as the first element of the list
    largest = lst[0]
    
    # Initialize the second largest number as 0
    second_largest_num = 0

    # Iterate over the list to find the largest and second largest numbers
    for i in lst:
        if i > largest:
            # Update second largest to the previous largest
            second_largest_num = largest
            # Update largest to the current number
            largest = i
        elif largest > i > second_largest_num:
            # Update second largest if the current number is between largest and second largest
            second_largest_num = i

    return second_largest_num


def second_smallest_v3(lst: List[int]) -> int:
    smallest = lst[0]
    second_smallest_num = float('inf')

    for i in lst:
        if i < smallest:
            second_smallest_num = smallest
            smallest = i
        elif smallest < i < second_smallest_num:
            second_smallest_num = i

    return second_smallest_num


def main():
    lst = [3, 6, 8, 10, 10, 1, 2, 1]
    print(second_largest(lst))
    print(second_smallest(lst))

    print("-------------------------------------------------------")
    print(second_largest_v2(lst))
    print(second_smallest_v2(lst))
    print("-------------------------------------------------------")
    print(second_largest_v3(lst))
    print(second_smallest_v3(lst))


if __name__ == "__main__":
    main()
