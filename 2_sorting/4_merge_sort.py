
# for [3, 2, 1, 5, 4] , l = 0, r = 4 


def merge_sort(arr, l, r):

    if l >= r:
        return
    
    mid = (l + r) // 2

    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    
    left_arrow = l
    right_arrow = mid + 1

    temp = []

    while left_arrow <= mid and right_arrow <= r:

        if arr[left_arrow] <= arr[right_arrow]:
            temp.append(arr[left_arrow])
            left_arrow += 1
        else:
            temp.append(arr[right_arrow])
            right_arrow += 1

    while left_arrow <= mid:
        temp.append(arr[left_arrow])
        left_arrow += 1
        
    while right_arrow <= r:
        temp.append(arr[right_arrow])
        right_arrow += 1

    for i in range(l, r+1):
        arr[i] = temp[i - l]



def main():
    arr = [12, 0, 11, 13, 5, 6, 7, 5]
    merge_sort(arr, 0, len(arr)-1)

    arr2 = [3, 2]
    merge_sort(arr, 0, len(arr)-1)

    arr3 = [3]
    merge_sort(arr, 0, len(arr)-1)

    print(arr)
    print(arr2)
    print(arr3)



if __name__ == "__main__":
    main()

