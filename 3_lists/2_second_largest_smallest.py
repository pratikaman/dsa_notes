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
    largest = lst[0]

    for i in lst:  # O(n)
        if i > largest:
            largest = i

    second_largest = float('-inf')

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
    largest = lst[0]
    second_largest_num = 0

    for i in lst:
        if i > largest:
            second_largest_num = largest
            largest = i
        elif largest > i > second_largest_num:
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
