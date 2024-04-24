

def print_to_n(n):
    if n == 0:
        return
    
    print_to_n(n-1)
    print(n)


def main():
    print_to_n(7)


if __name__ == "__main__":
    main()