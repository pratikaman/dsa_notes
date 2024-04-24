
# def extract_digits(n):
#     return [int(i) for i in str(n) ]


def extract_digits_hard(n):
    digits = []

    while n > 0:
        digits.append(n % 10)
        n = n // 10
    
    return digits



def main():
    # print(extract_digits(12345))
    print(extract_digits_hard(43634252))


if __name__ == "__main__":
    main()