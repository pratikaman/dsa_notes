def left_rotate_by_d(arr, d):
    # If d is greater than the length of the array,
    # we can reduce it to the remainder of d divided by the length of the array
    d = d % len(arr)

    temp = arr[:d]

    for i in range(d, len(arr)):
        arr[i - d] = arr[i]

    arr[-d:] = temp


def main():
    arr = [1, 2, 3, 4, 5, 3, 3, 1, 6]
    left_rotate_by_d(arr, 31)
    print(arr)


if __name__ == '__main__':
    main()
