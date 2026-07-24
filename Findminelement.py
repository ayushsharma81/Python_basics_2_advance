# Python3 program to find minimum element to remove so no common 
# element exist in both array

from collections import Counter

def minRemove(arr1, arr2):
    countA = Counter(arr1)
    countB = Counter(arr2)
    res = 0

    # Traverse through all common elements, and pick minimum
    # occurrence from two arrays
    for key in countA:
        if key in countB:
            res += min(countA[key], countB[key])

    return res

arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 4, 5, 8]

print(minRemove(arr1, arr2))
