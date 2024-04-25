

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr


def main():
    array = [64, 25, 12, 11, 99, 22, 11 , 3]
    print(bubble_sort(array))


if __name__ == "__main__":
    main()