 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    

    pivot = arr[0]

    less = [x for x in arr[1:] if x <= pivot]
    larger = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(larger)

    # Time complexity: O(n log n) in the average case, 
    # O(n^2) in the worst case if the array is already sorted


    # Space complexity:


def quick_sortV2(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)

        quick_sortV2(arr, low, partition_index - 1)
        quick_sortV2(arr, partition_index + 1, high)



def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high-1:
            i += 1

        while arr[j] > pivot and j >= low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j
    
def main():
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(quick_sort(arr))
    print("-------------------------------------------------------")
    arr2 = [3, 6, 8, 10, 1, 2, 1]
    quick_sortV2(arr2, 0, len(arr2) - 1)
    print(arr2)


if __name__ == "__main__":
    main()