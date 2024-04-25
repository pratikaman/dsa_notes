
def factorial_n(n):
    if n == 1 or n == 0:
        return 1
    
    return n * factorial_n(n-1)


def main():
    print(f"7 --->{factorial_n(7)}")
    print(f"10--->{factorial_n(10)}")
    print(f"5--->{factorial_n(5)}")
    print(f"0--->{factorial_n(0)}")
    print(f"3--->{factorial_n(3)}")

if __name__ == "__main__":
    main()