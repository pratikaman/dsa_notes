

def print_to_1(n):
    if n == 0:
        return
    
    print(n)
    print_to_1(n-1)
    


def main():
    print_to_1(7)


if __name__ == "__main__":
    main()