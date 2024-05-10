from typing import List

def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]


def sortArrvV2(arr: List[int]) -> int:
    max_elem = arr[0]

    for i in arr:
        if i > max_elem:
            max_elem = i
    
    return max_elem
    


def main():
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(sortArr(arr))

    print("-------------------------------------------------------")

    arr2 = [3, 6, 8, 10, 1, 2, 1]
    print(sortArrvV2(arr2))

if __name__ == "__main__":
    main()

