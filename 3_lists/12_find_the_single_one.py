
# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
# arr = [2,2,1]
# ans = 1

def find_single_one(arr):

    for i in range(len(arr)):

        count = 0

        for j in range(len(arr)):

            if arr[j] == arr[i]:
                count += 1

        if count == 1:
            return arr[i]
        
    return -1

    # Time complexity: O(n^2)
    # Space complexity: O(1)


def find_single_one_v2(arr):
    # using hash array


    # Step 1: Create a hash array

    # first find the max element in the array

    max_element = 0

    # max_element = max(arr)

    for i in arr:
        if i > max_element:
            max_element = i

    hash_arr = [0] * (max_element + 1) # [0, 0, 0, 0, 0, 0] if max_element = 5


    # Step 2: Traverse the array and increment the count of the element in the hash array

    for i in arr:
        hash_arr[i] += 1

    # Step 3: Traverse the hash array and return the element with count 1

    for i in arr:
        if hash_arr[i] == 1:
            return i
    
    return -1
    
    # Time complexity: O(n) + O(n) + O(n) = O(n)
    # Space complexity: O(max_element + 1)


def find_single_one_v3(arr):

    # Step 1: Create a dictionary

    hash_dict = {}

    # Step 2: Traverse the array and increment the count of the element in the dictionary
    for i in arr:
        hash_dict[i] = hash_dict.get(i, 0) + 1

    # Step 3: Traverse the dictionary and return the element with count 1
    for key, value in hash_dict.items():
        if value == 1:
            return key
    
    return -1

    # Time complexity: O(N*logM) + O(M), where M = size of the map i.e. M = (N/2)+1. N = size of the array.
    # We are inserting N elements in the map data structure and insertion takes logM time(where M = size of the map). 
    # So this results in the first term O(N*logM). The second term is to iterate the map and search the single element. 
    # In Java, HashMap generally takes O(1) time complexity for insertion and search. 
    # In that case, the time complexity will be O(N) + O(M).

    # Note: The time complexity will be changed depending on which map data structure we are using. 
    # If we use unordered_map in C++, the time complexity will be O(N) for the best and average case instead of O(N*logM). 
    # But in the worst case(which rarely happens), it will be nearly O(N2).

    # Space complexity: O(M) as we are using a map data structure. Here M = size of the map i.e. M = (N/2)+1.



def find_single_one_v4(arr):
    xor = 0

    for i in arr:
        xor ^= i

    return xor

    # Time complexity: O(n)
    # Space complexity: O(1)



    
def main():
    arr = [4, 1, 2, 1, 2]
    print(find_single_one(arr))
    print('--------------------------------------------------------')

    arr2 = [4, 1, 2, 1, 2]
    print(find_single_one_v2(arr2))
    print('--------------------------------------------------------')

    arr3 = [4, 1, 2, 1, 2]
    print(find_single_one_v3(arr3))
    print('--------------------------------------------------------')

    arr4 = [4, 1, 2, 1, 2]
    print(find_single_one_v4(arr4))


if __name__ == "__main__":
    main()