def countRecur(coins, n, sum):
    
    # If sum is 0 then there is 1 solution
    if sum == 0:
        return 1

    if sum < 0 or n == 0:
        return 0

    # count is sum of solutions
    # (i) including coins[n-1] (ii) excluding coins[n-1]
    return countRecur(coins, n, sum - coins[n - 1]) + \
           countRecur(coins, n - 1, sum)


def count(coins, sum):
    return countRecur(coins, len(coins), sum)
    

if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 5
    print(count(coins, sum))
