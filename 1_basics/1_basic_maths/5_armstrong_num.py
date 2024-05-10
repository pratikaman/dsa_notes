import math

def check_armstrong(n):
    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
    For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    n2 = n
    sum = 0

    k = int(math.log10(n) + 1)

    while n > 0:
        sum += (n % 10) ** k
        n = n // 10

    return n2 == sum


def main():
    print(check_armstrong(153))
    print(check_armstrong(123))
    print(check_armstrong(370))
    print(check_armstrong(371))
    print(check_armstrong(40723423))

if __name__ == "__main__":
    main()

