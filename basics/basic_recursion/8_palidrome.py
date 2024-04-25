

def check_palidrome_naive_approach(strr):
    n = len(strr)

    arr = list(strr.lower())

    arr2 = arr[:]

    if n == 0:
        return False
    
    if n == 1:
        return True
    
    for i in range(0, n):

        if i >= n//2:
            break

        arr2[i], arr2[n-i-1] = arr2[n-i-1], arr2[i]

    
    return arr == arr2




# Leetcode 125
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def check_palidrome2(s):

    # create a list of characters from the string
    # remove all non-alphanumeric characters and convert to lowercase/uppercase
    clean_s = [char.lower() for char in s if char.isalnum()]


    n = len(clean_s)

    if n == 0:
        return True
    
    if n == 1:
        return True
    
    for i in range(0, n):


        if i >= n//2:
            break

        if clean_s[i] != clean_s[n-i-1]:
            return False

    
    return True


def main():
    strr = "madam"
    strr2 = "hello"
    strr3 = "Racecar"
    strr4 = "a"
    strr5 = "ab"
    strr6 = "A man, a plan, a canal: Panama"

    print(strr, "------------>", check_palidrome_naive_approach(strr))
    print(strr2, "------------>", check_palidrome_naive_approach(strr2))
    print(strr3, "------------>", check_palidrome_naive_approach(strr3))
    print(strr4, "------------>", check_palidrome_naive_approach(strr4))
    print(strr5, "------------>", check_palidrome_naive_approach(strr5))
    print(strr6, "------------>", check_palidrome_naive_approach(strr6))

    print("-----------------------------------------------------------------")

    print(strr, "------------>", check_palidrome2(strr))
    print(strr2, "------------>", check_palidrome2(strr2))
    print(strr3, "------------>", check_palidrome2(strr3))
    print(strr4, "------------>", check_palidrome2(strr4))
    print(strr5, "------------>", check_palidrome2(strr5))
    print(strr6, "------------>", check_palidrome2(strr6))



if __name__ == "__main__":
    main()