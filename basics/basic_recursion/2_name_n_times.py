

def print_name_n_times(name, i, n):
    if i > n:
        return
    
    print(name)
    print_name_n_times(name, i + 1, n)


def print_name_n_times_v2(name, n):
    if n == 0:
        return
    
    print_name_n_times_v2(name, n-1)
    print(name)


def main():
    print_name_n_times("John", 1, 7)
    print("----------------------------------------------------")
    print_name_n_times_v2("John", 7)


if __name__ == "__main__":
    main()