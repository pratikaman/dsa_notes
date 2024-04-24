import math

def check_prime_easy(n):
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    
    return True if count == 2 else False


def check_prime_hard(n):
    count = 0

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1

            if i != n // i:
                count += 1

    
    return True if count == 2 else False


def main():
    print(f"4 - {check_prime_easy(4)}")
    print(f"5 - {check_prime_easy(5)}")
    print(f"6 - {check_prime_easy(6)}")
    print(f"7 - {check_prime_easy(7)}")
    print(f"33 - {check_prime_easy(33)}")

    print("---------------------------------------------------")
    print(f"4 - {check_prime_hard(4)}")
    print(f"5 - {check_prime_hard(5)}")
    print(f"6 - {check_prime_hard(6)}")
    print(f"7 - {check_prime_hard(7)}")
    print(f"33 - {check_prime_hard(33)}")


if __name__ == "__main__":
    main()
