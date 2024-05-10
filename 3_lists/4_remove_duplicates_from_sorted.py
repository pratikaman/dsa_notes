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
