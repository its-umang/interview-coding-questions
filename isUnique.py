# T:O(n) S:O(n)
# You can say constant n(<128 always for ASCII)
def isUnique(str):
    if(len(str)>128):
        return False
    b = [0]*128
    for i in str:
        if(b[ord(i)]==1):
            return False
        b[ord(i)]=1
    return True

# T:O(n) S:O(1)
# Only Lower Values
def isUniqueSpace(str):
    checker = 0
    str = str.lower()
    for i in str:
        val = ord(i)-ord('a')
        if((checker&(1<<val))>0):
            return False
        checker |= (1<<val)
    return True

# If no additional data structure to use
# (i): O(n^2): Compare every element with others
# (ii): O(nlogn): Sort the string than linear comparison
#       This may use extra space

if __name__ == "__main__":
    s = "ABC"
    t = "ABCa"
    u = "ABCaB"
    print(isUnique(s))
    print(isUnique(t))
    print(isUnique(u))