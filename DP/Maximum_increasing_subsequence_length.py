def lis(arr,n):
    lis = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i]:lis[i] = max(lis[i],lis[j]+1)  # we are  thinking that upto j the length of the subseq. is lis[j] and we are doing +1
        print("")
    return max(lis)
print(lis([10, 22, 9, 33, 21, 50, 41, 60, 80],9))