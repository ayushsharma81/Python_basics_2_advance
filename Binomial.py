# Python implementation to find 
# Binomial Coefficient using recursion

# Returns value of Binomial Coefficient C(n, k)
def binomialCoeff(n, k):
  
    # k can not be grater then n so we
    # return 0 here
    if k > n:
        return 0
      
    # base condition when k and n are equal 
    # or k = 0
    if k == 0 or k == n:
        return 1

    # Recursive add the value 
    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)

n = 5
k = 2
print(binomialCoeff(n, k))
