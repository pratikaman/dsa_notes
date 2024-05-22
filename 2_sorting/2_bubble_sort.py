

def bubble_sort(arr):
    
    # Iterate through the array from the last element to the second element
    for i in range(len(arr) - 1, 0, -1):
        # Iterate through the array from the first element to the i-th element
        for j in range(0, i):
            # Compare adjacent elements and swap them if necessary
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr


def main():
    array = [64, 25, 12, 11, 99, 22, 11 , 3]
    print(bubble_sort(array))
    array2 = [5, 1]
    print(bubble_sort(array2))


if __name__ == "__main__":
    main()