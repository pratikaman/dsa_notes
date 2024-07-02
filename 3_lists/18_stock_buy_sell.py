# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock. 
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

import sys

def max_profit(prices):

    profit = 0

    for i in range(len(prices)):

        for j in range(i+1, len(prices)):

            profit = max(profit, prices[j] - prices[i])

        
    return profit

    # Time Complexity: O(N2), where N = size of the array.
    # Space Complexity: O(1)


def max_profit_v2(prices):
    profit = 0
    
    minimum = sys.maxsize

    for i in range(len(prices)):
        
        minimum = min(minimum, prices[i])
        
        profit = max(profit, prices[i] - minimum)

    return profit

    # Time Complexity: O(N), where N = size of the array.
    # Space Complexity: O(1)


def main():
    
        prices = [2,3,5,7,1,9]

        prices2 = [7,6,4,3,1]
    
        print(max_profit(prices))
        print("-----------------------")
        print(max_profit(prices2))

        print("-----------------------")
        print(max_profit_v2(prices))
    


if __name__ == "__main__":
    main()