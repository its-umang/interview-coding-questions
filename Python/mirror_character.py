# Given a string and a number N, we need to mirror the characters from N-th position 
# up to the length of the string in the alphabetical order. 
# In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.
# Without using dictionary

def mirror_character(str, n):
    str = str.lower()
    final = ['']*len(str)
    for i in range(len(str)):
        if(i>=n-1):
            # val = ord('a')+25-(ord(str[i])-ord('a'))
            val = ord('z')-(ord(str[i])-ord('a'))
            final.append(chr(val))
        else:
            final.append(str[i])
    return ''.join(final)

if __name__ == "__main__":
    str = 'pennsylvania'
    str = 'paradox'
    n = 3
    print(str)
    print(mirror_character(str, n))
    pass