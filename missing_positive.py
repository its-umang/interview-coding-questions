def find(arr):
    n = len(arr)
    if(n==0):
        return 1
    # if(n==1):
        # return 1 if arr[0]!=1 else 2
    c1 = 0
    for i in range(n):
        if(arr[i]==1):
            c1 = 1
        elif(arr[i]<=0 or arr[i]>n):
            arr[i]=1

    if(c1==0):
        return 1

    for i in range(n):
        idx = abs(arr[i])-1
        if(arr[idx]>0):
            arr[idx] = -1*arr[idx]

    for i in range(n):
        if(arr[i] > 0):
            return i+1
        
    return n+1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 9]
    print(find(arr))