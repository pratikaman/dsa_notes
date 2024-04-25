import math

def check_armstrong(n):
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

