
# Given an array and a sum k (positive).

# Example:
# Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
# Result: 3
# Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

def longest_subarray(arr, k):
    
    longest_subarray = 0


    for i in range(len(arr)):

        for j in range(i, len(arr)):

            sum = 0

            for m in range(i, j+1):
                sum += arr[m]
            
            if sum == k:
                longest_subarray = max(longest_subarray, j-i+1)
        
    return longest_subarray

    # time complexity: O(n^3)
    # space complexity: O(1)



def longest_subarray_v2(arr, k):

    longest_subarray = 0

    for i in range(len(arr)):
        
        sum = 0

        for j in range(i, len(arr)):

            sum += arr[j]

            if sum == k:
                longest_subarray = max(longest_subarray, j-i+1)
        
    return longest_subarray

    # time complexity: O(n^2)
    # space complexity: O(1)


# Using Hashing
# This it optimal solution if there are 0s or negative numbers in the array.
# else there one more optimal solution using two pointer approach.
def longest_subarray_v3(arr, k):

    preSumMap = {}
    sum = 0
    longest_sub_array = 0

    for i in range(len(arr)):

        # calculate the prefix sum till index i:
        sum += arr[i]

        # if the sum = k, update the maxLen:
        if sum == k:
            longest_sub_array = max(longest_sub_array, i+1)

        # calculate the sum of remaining part i.e. x-k:
        sumOfRemainder = sum - k

        # Calculate the length and update maxLen:
        if sumOfRemainder in preSumMap:
            longest_sub_array = max(longest_sub_array, i - preSumMap[sumOfRemainder])

        # Finally, update the map checking the conditions:
        if sum not in preSumMap:
            preSumMap[sum] = i

        
    return longest_sub_array

    # time complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
    # spaca complexity: O(N) as we are using a map data structure.


# Using two pointer approach
def longest_subarray_v4(arr, k):

    # pointers
    left, right = 0, 0

    sum = arr[0]

    longest_sub_array = 0

    while right < len(arr):

        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while sum > k and left <= right:
            sum -= arr[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if sum == k:
            longest_sub_array = max(longest_sub_array, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < len(arr):
            sum += arr[right]
    
    return longest_sub_array

    # Time Complexity: O(2*N), where N = size of the given array.
    # Reason: The outer while loop i.e. the right pointer can move up to index n-1(the last index). 
    # Now, the inner while loop i.e. the left pointer can move up to the right pointer at most. 
    # So, every time the inner loop does not run for n times rather it can run for n times in total. 
    # So, the time complexity will be O(2*N) instead of O(N2).

    # Space Complexity: O(1) as we are not using any extra space.

            

def main():
    arr = [2,3,5,1,9,1,4]
    arr2 = [2,0,0,3]
    k = 10
    k2 = 3


    print(longest_subarray(arr, k))
    print('------------------------------------------')

    print(longest_subarray_v2(arr, k))
    print('------------------------------------------')

    print(longest_subarray_v3(arr, k))
    print(longest_subarray_v3(arr2, k2))
    print('------------------------------------------')

    print(longest_subarray_v4(arr, k))
    print('------------------------------------------')


if __name__ == "__main__":
    main()
            