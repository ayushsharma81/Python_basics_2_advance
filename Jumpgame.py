import sys

# Returns minimum jumps needed from index i to reach end
def minJumpsRecur(i, arr):
    if i >= len(arr) - 1:
        return 0

    ans = sys.maxsize

    # Try all reachable positions from i
    for j in range(i + 1, min(i + arr[i] + 1, len(arr))):
        val = minJumpsRecur(j, arr)
        if val != sys.maxsize:
            ans = min(ans, 1 + val)

    return ans

def minJumps(arr):
    ans = minJumpsRecur(0, arr)
    return -1 if ans == sys.maxsize else ans 

if __name__ == "__main__": 
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(minJumps(arr))
