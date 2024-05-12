

def linear_search(arr, num):
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i

    return -1


def main():
    arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    num = 5
    print(linear_search(arr, num))
    print('--------------------------------------------------')
    num2 = 56
    print(linear_search(arr, num2))


if __name__ == '__main__':
    main()
