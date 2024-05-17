
# Problem Statement: Given an array of N integers, write a program 
# to return an element that occurs more than N/2 times in the given array.
# You may consider that such an element always exists in the array.

from collections import Counter


def majority_elem(arr):

    hash_map = {}

    for i in arr:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    for key, value in hash_map.items():
        if value > len(arr) // 2:
            return key
    
    return None

    # Time complexity: O(n log n) + O(n)
    # Space complexity: O(n)


def majority_elem_v2(arr):

    n = len(arr)
    
    for i in range(n):

        count = 0

        for j in range(n):

            if arr[j] == arr[i]:
                count += 1
            
        if count > n // 2:
            return arr[i]
        
    return None

    # Time complexity: O(n^2)
    # Space complexity: O(1)


# Using Counter class from collections module
def majority_elem_v3(arr):
    counter = Counter(arr)

    for num, count in counter.items():

        if count > len(arr) // 2:
            return num
        
    # Time Complexity: O(N*logN) + O(N), where N = size of the given array.
    # Reason: We are using a map data structure. Insertion in the map takes logN time. 
    # And we are doing it for N elements. So, it results in the first term O(N*logN). 
    # The second O(N) is for checking which element occurs more than floor(N/2) times. 
    # If we use unordered_map instead, the first term will be O(N) for the best and average case 
    # and for the worst case, it will be O(N2).


# using moore's voting algo
def majority_elem_v4(arr):

    ele = None

    count = 0

    for i in range(len(arr)):

        if count == 0:
            ele = arr[i]


        if arr[i] == ele:
            count += 1
        else:
            count -= 1

    if count == 0:
        return None
    
    count2 = 0

    for i in range(len(arr)):

        if arr[i] == ele:
            count2 += 1
    
    if count2 > len(arr) / 2 :
        return ele
    
    return None
    # Time Complexity: O(N) + O(N), where N = size of the given array.
    # Space Complexity: O(1) as we are not using any extra space.


def main():
    arr = [2, 3, 4, 1, 3, 3, 3]
    print(majority_elem(arr))
    print('----------------------------------')
    print(majority_elem_v2(arr))
    print('----------------------------------')
    print(majority_elem_v3(arr))
    print('----------------------------------')
    print(majority_elem_v4(arr))


if __name__ == "__main__":
    main()
