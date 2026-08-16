# Calculate the maximum stolen value recursively
def findMaxSumRec(arr, n):
	
    # If no houses are left, return 0.
    if n <= 0:
        return 0
  
  	# If only 1 house is left, rob it. 
    if n == 1:
        return arr[0]

    # Two Choices: Rob the nth house and do not rob the nth house 
    pick = arr[n - 1] + findMaxSumRec(arr, n - 2)
    notPick = findMaxSumRec(arr, n - 1)

    # Return the max of two choices
    return max(pick, notPick)

# Function to calculate the maximum stolen value
def findMaxSum(arr):
    n = len(arr)
    
    # Call the recursive function for n houses
    return findMaxSumRec(arr, n)

if __name__ == "__main__":
    arr = [6, 7, 1, 3, 8, 2, 4]
    print(findMaxSum(arr))
  
