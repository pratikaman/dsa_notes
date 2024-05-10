import math

def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count


# log10(n) approx equal to number of digits in n - 1
def count_digits_log(n):
    return int(math.log10(n) + 1)


# point to note: whenever there is a divison a, the time complexity is O(log N) (base a)

def main():
    print(count_digits(12345))
    print(count_digits(43634252)) 
    print(count_digits(1))
    print("-------------------")
    print(count_digits_log(12345))
    print(count_digits_log(43634252))
    print(count_digits_log(1))


if __name__ == "__main__":
    main()