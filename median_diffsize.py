def getMedian(arr1, arr2):
    if(len(arr1)>len(arr2)):
        arr1, arr2 = arr2, arr1
    x, y = len(arr1), len(arr2)
    low, high = 0, x
    while(low<=high):
        partX = (low+high)//2
        partY = (x+y+1)//2 - partX
        maxLeftX = arr1[partX-1] if partX > 0 else float('-inf')
        minRightX = arr1[partX] if partX != x else float('inf')
        maxLeftY = arr2[partY-1] if partY > 0 else float('-inf')
        minRightY = arr2[partY] if partY != y else float('inf')
        if(maxLeftX <= minRightY and maxLeftY <= minRightX):
            if((x+y)%2==0):
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.0
            else:
                return max(maxLeftX, maxLeftY)
        elif(maxLeftX > minRightY):
            high = partX - 1
        else:
            low = partX + 1

if __name__ == "__main__":
    arr1 = [1, 12, 15, 26, 38, 40]
    arr2 = [2, 13, 17, 30, 45]
    print(int(getMedian(arr1, arr2)))