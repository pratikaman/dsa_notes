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





def main():
    arr1 = [1, 2, 4, 4, 5, 8]
    arr2 = [3, 4, 5, 6, 7, 7]

    print(union(arr1, arr2))
    print("-----------------------------------------------")
    print(union2(arr1, arr2))


if __name__ == "__main__":
    main()
