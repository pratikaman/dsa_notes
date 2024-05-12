def move_zeroes_to_end(arr):
    temp = []

    # Copy all non-zero elements to temp
    for i in range(0, len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])

    # Copy all elements from temp to arr
    for i in range(0, len(temp)):
        arr[i] = temp[i]

    # Fill remaining elements with 0
    for i in range(len(temp), len(arr)):
        arr[i] = 0


def move_zeroes_to_end_v2(arr):
    # Initialize a variable j to 0. This will be used to keep track of the position where we need to move the non-zero elements.
    j = 0

    # Loop through the array from the start
    for i in range(0, len(arr)):
        # If we find a zero, we set j to the current index and break the loop.
        # This is because we want to start moving non-zero elements to the position of the first zero we find.
        if arr[i] == 0:
            j = i
            break

    # Now, we loop through the array again, starting from the position of the first zero we found.
    for i in range(j, len(arr)):
        # If we find a non-zero element, we swap it with the element at position j.
        # This effectively moves the non-zero element to the position of the zero, and the zero to the current position.
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            # We then increment j, so that the next
            # non-zero element we find will be moved to the next position where we have a zero.
            j += 1


def main():
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    move_zeroes_to_end(arr)
    print(arr)
    print('---------------------------------------------------')
    arr2 = [1, 2, 0, 4, 3, 0, 5, 0]
    move_zeroes_to_end_v2(arr2)
    print(arr2)


if __name__ == '__main__':
    main()
