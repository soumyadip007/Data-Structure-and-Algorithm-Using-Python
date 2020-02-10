def ispalin(str,a,b):
    str1 = str[a:b+1]
    str2 = str1[::-1]
    if str1!=str2:return False
    else:return True
str = str(input())
n = len(str)
dp = [[0 for i in range(n)]for i in range(n)]
for i in range(1,n):
    for j in range(0,n-i):
        if(ispalin(str,j,j+i)):dp[j][j+i] = 0;
        else:dp[j][j+i] = 1 + min(dp[j][j-1+i],dp[j+1][j+i]);
for i in range(0,n):
    for j in range(0,n):
        if(i<=j):print(dp[i][j],end=" ");
        else:print(" ",end=" ");
    print(" ");
print("Min cuts = ",dp[0][n-1])