def max_sum(arr,n):
    res = [0]*n
    res[0] = arr[0]
    for i in range(1,n):
        res[i] = arr[i]
        for j in range(i):
            if arr[j]<arr[i]:res[i] = max(res[i],res[j]+arr[i])
    return max(res)
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(max_sum(arr,n))

