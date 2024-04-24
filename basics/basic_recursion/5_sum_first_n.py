
# not using summation formula.

def sum_first_n(n):
    if n == 0:
        return 0
    
    summ = n + sum_first_n(n-1)

    return summ
 

def main():
    print(f"7 --->{sum_first_n(7)}")
    print(f"10--->{sum_first_n(10)}")
    print(f"5--->{sum_first_n(5)}")
    print(f"0--->{sum_first_n(0)}")

if __name__ == "__main__":
    main()
