

def recursive_count(n):
    if n == 1:
        return [1]
    
    a = recursive_count(n - 1)
    a.append(n)
    return a



def main():
    print(recursive_count(5))
    print(recursive_count(10))
    print(recursive_count(18))


if __name__ == "__main__":
    main()