def left_rotate_by1(arr):
    temp = arr[0]

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[-1] = temp


def main():
    arr = [1, 2, 3, 4, 5]
    left_rotate_by1(arr)
    print(arr)


if __name__ == '__main__':
    main()
