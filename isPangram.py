# Pangram Contains all alphabets letters

def isPangram(str):
    str = str.lower()
    if(len(str)<26):
        return False
    b = [0]*26
    str = ''.join(str.split())
    for i in str:
        # print(ord(i)-ord('a'))
        b[ord(i)-ord('a')]+=1
    for i in range(len(b)):
        # print(b[i])
        if(b[i]==0):
           return False
    return True

if __name__ == "__main__":
    # str = "Hhe quick brown fox jumps over she lazy dog"
    str = "The quick brown fox jumps over the lazy dog"
    print(isPangram(str))