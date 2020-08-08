def isAnagram(s1, s2):
    if(len(s1)!=len(s2)):
        return False
    
    s1 = s1.lower()
    s2 = s2.lower()

    letters = [0]*(1<<8)
    # Convert to list of characters
    s1 = list(s1)
    s2 = list(s2)
    for i in s1:
        # print(ord(i))
        letters[ord(i)]+=1
    for i in s2:
        letters[ord(i)]-=1
    for i in letters:
        if(i!=0):
            return False

    return True

if __name__ == "__main__":
    print(isAnagram("",""))
    print(isAnagram("Abb","bab"))
    print(isAnagram("abbc","acc"))
    print(isAnagram("aaaa","aaad"))