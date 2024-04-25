

def all_divisors(n):
    divisors = []

    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    
    return divisors


def main():
    n = 3
    divisors = all_divisors(n)
    print(divisors)
    print(sum(divisors))


if __name__ == "__main__":
    main()