

# Problem: Find the nth Fibonacci number.
# Using for loop. Dont use in interview.
# counting starts from 0 index

def nth_fibonacci_v1(n):
    if n <= 1:
        return n
    
    val = []
    
    for i in range(0, n+1):

        if i <= 1:
            val.append(i)
        else:
            val.append(val[i-1] + val[i-2])

    return val[-1]

# Using recursion. Use this in interview.
def nth_fibonacci_v2(n):
    if n <= 1:
        return n
    
    last = nth_fibonacci_v2(n-1)
    second_last = nth_fibonacci_v2(n-2)

    return last + second_last

        

def main():

    print("----------------------------Using for loop--------------------")
    for i in range(0, 8):
        print(f"n{i} = {nth_fibonacci_v1(i)}")

    print("----------------------------Using recursion--------------------")
    for i in range(0, 8):
        print(f"n{i} = {nth_fibonacci_v2(i)}")



if __name__ == "__main__":
    main()
