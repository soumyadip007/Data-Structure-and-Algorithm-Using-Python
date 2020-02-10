for _  in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n==1:print(arr[0])
    elif n==2:print(max(arr[0],arr[1]))
    else:
        dp = [arr[0],max(arr[0],arr[1])]
        for i in range(2,n):dp.append(max(dp[i-1],arr[i]+dp[i-2]))
        print(dp[n-1])