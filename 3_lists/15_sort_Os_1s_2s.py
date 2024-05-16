
# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
# Write a program to in-place sort the array without using inbuilt sort functions. 
# ( Expected: Single pass-O(N) and constant space)


def sort_0s_1s_2s(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in arr:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1

    for i in range(count_0):
        arr[i] = 0

    for i in range(count_0, count_0 + count_1):
        arr[i] = 1

    for i in range(count_0 + count_1, len(arr)):
        arr[i] = 2

    # Time Complexity: O(N) + O(N), where N = size of the array. 
    # First O(N) for counting the number of 0’s, 1’s, 2’s, and second O(N) for placing them correctly in the original array.

    # Space Complexity: O(1) as we are not using any extra space.



# Deautch National Flag Algorithm
def sort_0s_1s_2s_V2(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:

        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
        # Time Complexity: O(N), where N = size of the given array.
        # Reason: We are using a single loop that can run at most N times.

        # Space Complexity: O(1) as we are not using any extra space.


def main():
    arr = [0, 1, 2, 0, 1, 2]
    sort_0s_1s_2s(arr)
    print(arr)

    print('-----------------------------------------------------')
    arr2 = [0, 1, 2, 0, 1, 2]
    sort_0s_1s_2s_V2(arr2)
    print(arr2)

if __name__ == "__main__":
    main()