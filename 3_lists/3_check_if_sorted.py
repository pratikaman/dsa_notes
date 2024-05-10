import operator


def check_sorted(arr, order):
    op = operator.lt if order == 'asc' else operator.gt

    for i in range(1, len(arr)):
        if op(arr[i], arr[i - 1]):
            return False

    return True


def main():
    arr = [1, 2, 3, 4, 5]
    print(check_sorted(arr, 'asc'))  # True
    print(check_sorted(arr, 'desc'))  # False
    print('-----------------------------------------------------------')
    arr2 = [5, 4, 3, 2, 1]
    print(check_sorted(arr2, 'asc'))  # False
    print(check_sorted(arr2, 'desc'))  # True
    print('-----------------------------------------------------------')
    arr3 = [5, 4, 3, 2, 1]
    print(check_sorted(arr3, 'desc'))  # True
    print(check_sorted(arr3, 'asc'))  # False
    print('-----------------------------------------------------------')
    arr4 = [1, 2, 3, 4, 5]
    print(check_sorted(arr4, 'desc'))  # False
    print(check_sorted(arr4, 'asc'))  # True
    print('-----------------------------------------------------------')
    arr5 = [1, 6, 4, 2, 1]
    print(check_sorted(arr5, 'asc'))  # False
    print(check_sorted(arr5, 'desc'))  # False
    print('-----------------------------------------------------------')
    arr6 = [1, 1, 6, 7, 10]
    print(check_sorted(arr6, 'asc'))  # True
    print(check_sorted(arr6, 'desc'))  # False


if __name__ == '__main__':
    main()
