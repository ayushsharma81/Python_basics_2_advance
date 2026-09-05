import sys

    def updateBIT(BITree, n, index, val):
        index += 1  # Convert 0-indexed to 1-indexed

        while index <= n:
            BITree[index] += val
            index += index & (-index)  # Move to next ancestor

    def getSum(BITree, index):
        sum = 0
        index += 1  # Convert 0-indexed to 1-indexed

        while index > 0:
            sum += BITree[index]
            index -= index & (-index)  # Move to parent node
        return sum

    def constructBITree(arr, n):
        BITree = [0] * (n + 1)

        for i in range(n):
            GFG.updateBIT(BITree, n, i, arr[i])

        return BITree

if __name__ == "__main__":
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(freq)

    # Build the BIT
    BITree = GFG.constructBITree(freq, n)
    print("Sum of elements in arr[0..5] is:", GFG.getSum(BITree, 5))

    # Update operation: add 6 to freq[3]
    delta = 6
    GFG.updateBIT(BITree, n, 3, delta)
    
    print("Sum of elements in arr[0..5] after update is:", GFG.getSum(BITree, 5))
