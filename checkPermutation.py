# T:O(n) S:O(n)
# Again you can say constant(<128)
def checkPermutation(s1, s2):
    if(len(s1)!=len(s2)):
        return False
    
    b = [0]*128
    for i in s1:
        b[ord(i)]+=1
    for i in s2:
        b[ord(i)]-=1
        if(b[ord(i)]<0):
            return False
    return True

# Brute Force
# Sort both the string if of same size ofcourse
# Compare every element found diff -> False

if __name__ == "__main__":
    s1 = 'dog'
    s2 = 'GOd'
    print(checkPermutation(s1 ,s2))