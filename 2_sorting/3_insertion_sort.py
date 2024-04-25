

def insertion_sort(arr):

    for i in range(0, len(arr)):

        for j in range(i, 0, -1):

            if arr[j] < arr[j-1]:
                
                arr[j], arr[j-1] = arr[j-1], arr[j]
        
    return arr


def main():
    arr = [5, 2, 4, 6, 1, 3, 33, 22, 11, 44, 55, 77, 88, 99, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(insertion_sort(arr))


if __name__ == "__main__":
    main()