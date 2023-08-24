def fib(n):
    dp=[0,1,1] #Initial values of the series
    for i in range(3,n):
        next_term=dp[i-3]+dp[i-2]+dp[i-1]
        dp.append(next_term)
    return dp
n=int(input("How many terms?:"))
answer=fib(n)
print(answer) 

# Time Complexity: O(n)
# Space Complexity: O(n)