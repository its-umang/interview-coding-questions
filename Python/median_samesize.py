def median(arr, n):
    if(n%2==0):
        return (arr[int(n/2)]+arr[int((n/2)-1)])/2
    else:
        return arr[int(n/2)]
    pass

def getMedian(arr1, arr2):
    n = len(arr1)
    if(n==0):
        return -1
    elif(n==1):
        return (arr1[0]+arr2[0])/2
    elif(n==2):
        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)
        if(m1>m2):
            if(n%2==0):
                return getMedian(arr1[0:int(n/2)+1], arr2[int(n/2)-1:])
            else:
                return getMedian(arr1[0:int(n/2)+1], arr2[int(n/2):])
        else:
            if(n%2==0):
                return getMedian(arr1[int(n/2)-1:], arr2[0:int(n/2)+1:])
            else:
                return getMedian(arr1[int(n/2):], arr2[0:int(n/2)+1])

if __name__ == "__main__":
    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 13, 17, 30, 45]
    print(int(getMedian(arr1, arr2)))