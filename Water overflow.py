# Python program to find amount  
# of water in a given glass Using Dynamic Programming

def waterOverflow(k, r, c):
    
    # DP matrix to simulate water flow in glasses
    memo = [[0.0 for _ in range(r)] for _ in range(r)]
    
    # Initial water in top glass
    memo[0][0] = k
    
    # Simulate water flow through triangle
    for row in range(r - 1):
        for col in range(row + 1):
            
            # Calculate water overflow
            excess = max(0.0, memo[row][col] - 1.0)
            
            # Distribute excess water
            if excess > 0:
                
                # Cap current glass
                memo[row][col] = 1.0
                
                # Flow to bottom glasses
                memo[row + 1][col] += excess / 2.0
                memo[row + 1][col + 1] += excess / 2.0
    
    # Return water in target glass
    return min(1.0, memo[r - 1][c - 1])


if __name__ == "__main__":
    k = 3
    r = 2
    c = 1
    
    waterAmount = waterOverflow(k, r, c)
    print(waterAmount)
