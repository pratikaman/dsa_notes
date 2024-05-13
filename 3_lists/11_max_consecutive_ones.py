
# arr = [1,1,0,1,1,1,0,1,1]
# ans = 3

def max_consecutive_ones(arr):

    max_count = 0
    count = 0

    for i in arr:
        if i == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
            

    return max_count


def main():
    arr = [1,1,0,1,1,1,0,1,1]
    print(max_consecutive_ones(arr))


if __name__ == '__main__':
    main()