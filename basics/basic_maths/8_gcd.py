

def find_gcd(a, b):
    min_num = min(a, b)

    gcd = 1

    for i in range(1, min_num+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    return gcd


def find_gcd_v2(a, b):

    min_num = min(a, b)

    gcd = 1

    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    
    return gcd


# Using euclidean algorithm
# GCD(a, b) = GCD(a - b, b) if a > b
# GCD(a, b) = GCD(a % b, b) if a > b

def find_gcd_v3(a, b):

    if a == 0 :
        return b
    elif b == 0:
        return a
    else:
        return find_gcd_v3(abs(a-b), min(a,b))
    
def find_gcd_v4(a, b):

    gt = max(a, b)
    lt = min(a, b) 

    if b == 0 :
        return a
    elif a == 0:
        return b
    else:
        return find_gcd_v4(gt % lt, lt)


def main():

    print(f"12, 20 --- {find_gcd(12, 20)}")
    print(f"15, 5 --- {find_gcd(15, 5)}")
    print(f"100, 1000 --- {find_gcd(100, 1000)}")
    print(f"23, 42 --- {find_gcd(23, 42)}")

    print("---------------------------------------------------------------------------")
    print(f"12, 20 --- {find_gcd_v2(12, 20)}")
    print(f"15, 5 --- {find_gcd_v2(15, 5)}")
    print(f"100, 1000 --- {find_gcd_v2(100, 1000)}")
    print(f"23, 42 --- {find_gcd_v2(23, 42)}")

    print("---------------------------------------------------------------------------")
    print(f"12, 20 --- {find_gcd_v3(12, 20)}")
    print(f"15, 5 --- {find_gcd_v3(15, 5)}")
    print(f"100, 1000 --- {find_gcd_v3(100, 1000)}")
    print(f"23, 42 --- {find_gcd_v3(23, 42)}")

    print("---------------------------------------------------------------------------")
    print(f"12, 20 --- {find_gcd_v4(12, 20)}")
    print(f"15, 5 --- {find_gcd_v4(15, 5)}")
    print(f"100, 1000 --- {find_gcd_v4(100, 1000)}")
    print(f"23, 42 --- {find_gcd_v4(23, 42)}")



if __name__ == "__main__":
    main()