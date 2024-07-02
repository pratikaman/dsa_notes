

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
def check_palidrome2(s: str) -> bool:
    """
    Determines if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Create a list of characters from the string, removing all non-alphanumeric characters and converting to lowercase
    clean_s: list | None = [char.lower() for char in s if char.isalnum()]

    n = len(clean_s)

    # An empty string is considered a palindrome
    if n == 0:
        return True
    
    # A single character string is considered a palindrome
    if n == 1:
        return True
    
    # Check if the string is a palindrome by comparing characters from both ends
    for i in range(0, n):

        # if pointer crosses the middle, the string is not a palindrome
        if i >= n // 2:
            break

        # If the characters do not match, the string is not a palindrome
        if clean_s[i] != clean_s[n - i - 1]:
            return False

    # If all characters match, the string is a palindrome
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