def reverse_number_easy(n):
    return int(str(n)[::-1])


def reverse_number(n):
    rev = []
    # rev = 0


    


    while n > 0:
        # rev = rev * 10 + n % 10  # rev*10 + last digit
        # n = n // 10

        rev.append(n % 10)
        n = n // 10

    # return rev
    return int("".join(map(str, rev)))





def main():
    print(reverse_number_easy(12345))
    print(reverse_number_easy(43634252))
    print(reverse_number_easy(1))

    print("------------")
    print(reverse_number(12345))
    print(reverse_number(43634252))
    print(reverse_number(1))



if __name__ == "__main__":
    main()