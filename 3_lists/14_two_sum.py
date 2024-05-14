# Given an array of integers and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. 
#              Otherwise, we will return [-1, -1].

def two_sum(num, arr):
    

    for i in range(len(arr)):

        indices = [i]
        sum = arr[i]

        for j in range(i+1, len(arr)): # We are starting from i+1 as we don't want to consider the same element twice.

            if sum + arr[j] == num:
                indices.append(j)
                return indices
    
    return [-1, -1]

    # Time Complexity: O(N2), where N = size of the array.
    # Reason: There are two loops(i.e. nested) each running for approximately N times.

    # Space Complexity: O(1) as we are not using any extra space.


# Using hashing
def two_sum_v2(num, arr):
    hash_map = {}
    indices = []

    for i in range(len(arr)):
        if num - arr[i] in hash_map:
            indices.append(hash_map[num - arr[i]])
            indices.append(i)
            return indices
        else:
            hash_map[arr[i]] = i
        
    return [-1, -1]
    # Time Complexity: O(N), where N = size of the array.
    # Reason: The loop runs N times in the worst case and searching in a hashmap takes O(1) generally. 
    # So the time complexity is O(N).

    # Note: In the worst case(which rarely happens), the unordered_map takes O(N) to find an element. 
    # In that case, the time complexity will be O(N2). 
    # If we use map instead of unordered_map, 
    # the time complexity will be O(N* logN) as the map data structure takes logN time to find an element.

    # Space Complexity: O(N) as we use the map data structure.



# Note: We have optimized this problem enough. 
# But if in the interview, we are not allowed to use the map data structure, 
# then we should move on to the following approach i.e. two pointer approach.
# This approach will have the same time complexity as the better approach.

# two pointer approach
def two_sum_v3(num, arr):
    arr.sort()  # Sort the array in ascending order
    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == num:
            return "YES"
        elif sum < num:
            left += 1  # Move the left pointer to potentially increase the sum
        else:
            right -= 1  # Move the right pointer to potentially decrease the sum
    return "NO"

    # Time Complexity: O(N) + O(N*logN), where N = size of the array.
    # Reason: The loop will run at most N times. And sorting the array will take N*logN time complexity.

    # Space Complexity: O(1) as we are not using any extra space.

# Note: For variant 2, we can store the elements of the array along with its index in a new array. 
# Then the rest of the code will be similar. 
# And while returning, we need to return the stored indices instead of returning “YES”. 
# But for this variant, the recommended approach is approach 2 i.e. hashing approach.

def main():
    arr = [11, 2, 15, 7]
    num = 9

    print(two_sum(num, arr))
    print(two_sum_v2(num, arr))
    print(two_sum_v3(num, arr))


if __name__ == "__main__":
    main()
