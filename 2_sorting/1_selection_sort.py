
def selection_sort(array):
    # Create a copy of the input array
    arr = array[:]


    # Iterate over each element in the array
    for i in range(0, len(arr)):
        # Assume the current element is the minimum value
        min_val_index = i


        # Find the index of the minimum value in the remaining unsorted portion of the array
        for j in range(i, len(arr)):
            if arr[j] < arr[min_val_index]:
                min_val_index = j

        # Swap the current element with the minimum value
        arr[i], arr[min_val_index] = arr[min_val_index], arr[i]



    # Return the sorted array


    return arr

def main():
    # Test the selection_sort function
    array = [64, 25, 12, 99, 22, 11, 3]


    print(selection_sort(array))

if __name__ == "__main__":
    main()