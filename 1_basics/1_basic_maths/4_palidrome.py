def is_palindrome(s):
    return str(s) == str(s)[::-1]


def is_palindrome_hard(n):
    n2 = n
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    
    return n2 == rev


def main():
    print(is_palindrome(12321))
    print(is_palindrome(12345))
    print(is_palindrome(12321))
    print(is_palindrome(12345))
    print(is_palindrome(1331))
    print(is_palindrome(11))

    print("------------")

    print(is_palindrome_hard(12321))
    print(is_palindrome_hard(12345))
    print(is_palindrome_hard(12321))
    print(is_palindrome_hard(12345))
    print(is_palindrome_hard(1331))
    print(is_palindrome_hard(11))


if __name__ == "__main__":
    main()