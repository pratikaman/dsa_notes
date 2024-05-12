# Problem Statement: 
# Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
# Find the number(between 1 to N), that is not present in the given array.


# Example:
# Input Format:
#  N = 5, array = [1,2,4,5]
# Result:
#  3


def missing_number(n, arr):

    # For each element from 1 to n, check if it is present in the array

    for i in range(1, n+1):
        
        flag = 0

        for j in range(len(arr)):
            if i == arr[j]:
                flag = 1
                break

        if flag == 0:
            return i
        
    # time complexity: O(n^2)
    # space complexity: O(1)
    


def missing_number2(n, arr):

    # Create a hash table of size n+1, so that last index can be n
    # Initialize all the values to 0

    hash = [0] * (n+1) # for n = 5 [0, 0, 0, 0, 0, 0, 0]

    # For each element in the array, mark the index as 1
    for i in arr:
        hash[i] = 1
    
    # If the value is 0, return the index
    for i in range(1, n+1):
        if hash[i] == 0:
            return i
        
    # time complexity: O(n) + O(n) = O(n)
    # space complexity: O(n)


def missing_number3(n, arr):
     
    sum_of_n = n * (n+1) // 2
    sum_of_arr = sum(arr)

    return sum_of_n - sum_of_arr

    # time complexity: O(n)
    # space complexity: O(1)



# Core Idea: XOR (Exclusive OR)
# The code cleverly utilizes the properties of the XOR (exclusive OR) bitwise operator:

# XORing a number with itself results in 0: x ^ x = 0

# XORing a number with 0 results in the original number: x ^ 0 = x

# XOR is commutative and associative: x ^ y = y ^ x and (x ^ y) ^ z = x ^ (y ^ z)

# example-
# (1 ^ 2 ^ 3 ^ 4 ^ 6 ^ 7) ^ (1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7) = 5

def missing_number4(n, arr):
    xor1 = n
    xor2 = 0

    for i in range(n-1):
       
        # xor of elements in the array whose size is n-1,
        # so last index is n-2
        xor2 = xor2 ^ arr[i]

        # xor of elements from 1 to n-1
        xor1 = xor1 ^ (i+1)

    # xor1 = xor1 ^ n

    return xor1 ^ xor2




def main():
    n = 7
    arr = [1, 2, 3, 4, 6, 7]
    print(missing_number(n, arr))
    print('-----------------------------------------------')

    n2 = 7
    arr2 = [1, 2, 3, 4, 6, 7]
    print(missing_number2(n2, arr2))
    print('-----------------------------------------------')

    n3 = 7
    arr3 = [1, 2, 3, 4, 6, 7]
    print(missing_number3(n3, arr3))
    print('-----------------------------------------------')

    n4 = 7
    arr4 = [1, 2, 3, 4, 6, 7]
    print(missing_number4(n4, arr4))


if __name__ == "__main__":
    main()