# union of two sorted arrays


def union(arr1, arr2):
    freq = {}
    union = []


    # # O( (m+n)log(m+n) ) time complexity
    for i in arr1:
        freq[i] = freq.get(i,0) + 1
    
    for i in arr2:
        freq[i] = freq.get(i,0) + 1

    
    for key in freq:
        union.append(key)

    return union

def union2(arr1, arr2):
    s = set()

    # O( (m+n)log(m+n) ) time complexity
    for i in arr1:
        s.add(i)

    for i in arr2:
        s.add(i)

    return list(s)


# Approach:
# Take two pointers let’s say i,j pointing to the 0th index of arr1 and arr2.
# Create an empty vector for storing the union of arr1 and arr2.
# From solution 2 we know that the union is nothing but the distinct elements in arr1 + arr2 
# Let’s traverse the arr1 and arr2 using pointers i and j and insert the distinct elements found into the union vector.

# While traversing we may encounter three cases.

# ● arr1[ i ] == arr2[ j ] 
# Here we found a common element, so insert only one element in the union. Let’s insert arr[i] in union and increment i.

# NOTE: There may be cases like the element to be inserted is already present in the union, in that case, 
# we are inserting duplicates which is not desired. So while inserting always check whether the last element in the union vector is equal or not to the element to be inserted.
# If equal we are trying to insert duplicates, so don’t insert the element, else insert the element in the union.
# This makes sure that we are not inserting any duplicates in the union because we are inserting elements in sorted order.

# ● arr1[ i ] < arr2[ j ] so we need to insert arr1[ i ] in union.IF last element in  union vector is not equal to arr1[ i ],then insert in union else don’t insert. After checking Increment i.
# 
# ● arr1[ i ] > arr2[ j ] so we need to insert arr2[ j ] in union. IF the last element in the union vector is not equal to arr2[ j ], then insert in the union, else don’t insert. After checking Increment j. 

# After traversing if any elements are left in arr1 or arr2 check for condition and insert in the union.


def union3(arr1, arr2):
    i, j = 0, 0

    union_list = []

    while i < len(arr1) and j < len(arr2):

        # case 1 and case 2
        if arr1[i] <= arr2[j]:
            if len(union_list) == 0 or arr1[i] != union_list[-1]:
                union_list.append(arr1[i])
            i += 1
        

        # case 3
        elif arr1[i] > arr2[j]:
            if len(union_list) == 0 or arr2[j] != union_list[-1]:
                union_list.append(arr2[j])
            j += 1

    # If any elements left in arr1
    while i < len(arr1):
        if arr1[i] != union_list[-1]:
            union_list.append(arr1[i])
        i += 1

    # If any elements left in arr2
    while j < len(arr2):
        if arr2[j] != union_list[-1]:
            union_list.append(arr2[j])
        j += 1
        
    return union_list

def main():
    arr1 = [1, 2, 4, 4, 5, 8]
    arr2 = [3, 4, 5, 6, 7, 7]

    print(union(arr1, arr2))
    print("-----------------------------------------------")
    print(union2(arr1, arr2))
    print("-----------------------------------------------")
    print(union3(arr1, arr2))


if __name__ == "__main__":
    main()
