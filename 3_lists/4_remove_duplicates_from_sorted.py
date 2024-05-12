def remove_duplicates_from_sorted(arr):
    arr2 = []

    for i in range(0, len(arr)):
        if i == 0:
            arr2.append(arr[i])
        elif arr[i] != arr[i - 1]:
            arr2.append(arr[i])

    return arr2


def remove_duplicates_from_sorted2(arr):
    unique_set = set()

    for i in range(0, len(arr)):
        unique_set.add(arr[i])

    return list(unique_set)


def remove_duplicates_from_sorted3(arr):
    """
        This function removes duplicates from a sorted array in-place and returns the array.

        It uses two pointers, i and j, where i is the slow-runner and j is the fast-runner.

        The function starts by setting i to 0. Then it iterates over the array starting from the second element (index 1).

        For each element at index j, it checks if it is different from the element at index i.

        If it is, it means we have encountered a new unique element.

        In this case, it increments i and replaces the element at index i+1 with the element at index j.

        This effectively moves the unique elements to the front of the array.

        Finally, it returns a slice of the array up to the i+1 index, which contains all the unique elements.

        For example, if the input array is [2, 2, 3, 3, 4], the function will return [2, 3, 4].

        Note: This function assumes that the input array is sorted.

    """

    i = 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1

    return arr[:i + 1]


def main():
    arr = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5]
    print(remove_duplicates_from_sorted(arr))
    print('-------------------------------------')
    arr2 = [5, 6, 6, 7, 2, 2, 1]
    print(remove_duplicates_from_sorted(arr2))

    print('-------------------------------------')
    arr3 = [5, 6, 6, 7, 2, 2, 1]
    print(remove_duplicates_from_sorted2(arr3))

    print('-------------------------------------')
    arr4 = [5, 6, 6, 7, 2, 2, 1]
    print(remove_duplicates_from_sorted3(arr4))


if __name__ == '__main__':
    main()
