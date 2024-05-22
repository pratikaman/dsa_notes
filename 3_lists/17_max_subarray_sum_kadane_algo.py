
# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

import sys

def max_sum_subarr(arr):
    """
    Function to find the subarray with the maximum sum.
    """

    # Initialize the maximum sum to the minimum value.
    maxi = -sys.maxsize - 1

    n = len(arr)

    for first_pointer in range(n):

        for second_pointer in range(first_pointer, n):

            sum = 0
            

            # sum all the elements between the first_pointer and the second_pointer.
            for k in range(first_pointer, second_pointer+1):

                sum += arr[k]

            maxi = max(maxi, sum)

    
    return maxi
    
    # Time Complexity: O(N3), where N = size of the array.
    # Space Complexity: O(1)


def max_sum_subarr_v2(arr):

    maxi = -sys.maxsize - 1

    n = len(arr)

    for first_pointer in range(n):

        sum = 0

        for second_pointer in range(first_pointer, n):

            sum += arr[second_pointer]


            maxi = max(maxi, sum)

    
    return maxi

    # Time Complexity: O(N2), where N = size of the array.
    # Space Complexity: O(1)



# Using Kadane's Algorithm

def max_sum_subarr_v3(arr):

    maxi = arr[0]

    sum = 0

    for i in range(len(arr)):

        sum = sum + arr[i] if sum + arr[i] >= 0 else 0

        maxi = max(sum, maxi)
    
    return maxi

    # Time Complexity: O(N), where N = size of the array.
    # Space Complexity: O(1)


def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    print(max_sum_subarr(arr))
    print('------------------------------------------')
    print(max_sum_subarr_v2(arr))
    print('------------------------------------------')
    print(max_sum_subarr_v3(arr))



if __name__ == "__main__":
    main()


