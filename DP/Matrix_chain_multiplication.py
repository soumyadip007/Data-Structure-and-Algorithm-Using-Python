import sys
n  = int(input())
arr = list(map(int,input().split()))
dp = [[0 for i in range(n)]for j in range(n)]
for l in  range(2,n):
    for i in range(1,n-l+1):
        j,dp[i][j] = i+l-1,sys.maxsize
        for k in range(i,j):dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j])
print("Min no. of scalar mult = ",dp[1][n-1])