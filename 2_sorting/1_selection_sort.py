
# Here's how the selection process works:

# 1) Divide and Conquer: The input array is conceptually divided into two parts: the sorted portion at the beginning and the unsorted portion at the end. Initially, the sorted portion is empty.

# 2) Finding the Minimum/Maximum: The algorithm scans the unsorted portion to identify the smallest (or largest, depending on the desired sorting order) element.

# 3) Swapping: The identified minimum/maximum element is then swapped with the first element in the unsorted portion. This effectively places the selected element at its correct position in the sorted portion.

# 4) Iteration: The process is repeated for the remaining unsorted portion. In each iteration, the next smallest/largest element is found and swapped with the first element of the remaining unsorted portion.

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

    # Time complexity: O(n^2)
    # Precisely it is O( n(n+1)/2 ).


    # Space complexity: O(1)


def main():
    # Test the selection_sort function
    array = [64, 25, 12, 99, 22, 11, 3]


    print(selection_sort(array))

if __name__ == "__main__":
    main()