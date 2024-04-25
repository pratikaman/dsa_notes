

def reverse_array(l,r,arr):

    if len(arr) == 0:
        return []
    
    if len(arr) == 1:
        return arr
    

    # main condition to remember
    if l >= r:
        return
    
    arr[l], arr[r] = arr[r], arr[l]

    reverse_array(l+1, r-1, arr)

    return arr


def reverse_array2(i, arr):

    arr_len = len(arr)

    if arr_len == 0:
        return []
    
    if arr_len == 1:
        return arr
    

    # main condition to remember
    if i >= arr_len // 2:
        return
    
    arr[i], arr[arr_len-i-1] = arr[arr_len-i-1], arr[i]

    reverse_array2(i+1, arr)

    return arr



def reverse_array3(nums):

    n = len(nums)

    if n == 0:
        return []
    
    if n == 1:
        return nums

    for i in range(0,n):
        if i >= n//2:
            break
        
        nums[i], nums[n-i-1] = nums[n-i-1], nums[i]

    return nums


def main():

    arr = [1,2,3,4,5]
    arr2 = [1,2,3,4,5,6]

    arr3 = arr[:]
    arr4 = arr2[:]
    arr5 = arr[:]
    arr6 = arr2[:]
    arr7 = arr[:]
    arr8 = arr2[:]

    print(arr, "------>", reverse_array(0, len(arr3)-1, arr3))
    print(arr2, "------>", reverse_array(0, len(arr4)-1, arr4))

    print("------------------------------------------------------------------")

    print(arr, "------>", reverse_array2(0, arr5))
    print(arr2, "------>", reverse_array2(0, arr6))

    print("------------------------------------------------------------------")
    print(arr, "------>", reverse_array3(arr7))
    print(arr2, "------>", reverse_array3(arr8))
    


if __name__ == "__main__":
    main()