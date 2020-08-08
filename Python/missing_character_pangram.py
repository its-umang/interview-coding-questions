# Find Missing Character from Pangram
# Pangram Contains all alphabets letters

def missingPangram(str):
    str = str.lower()
    b = [0]*26
    str = ''.join(str.split())
    for i in str:
        b[ord(i)-ord('a')]+=1
    for i in range(len(b)):
        if(b[i]==0):
            print(chr(i+ord('a')), end='')
    
if __name__ == "__main__":
    # str = "The quick brown fox jumps over the lazy dog" # No Answer
    str = 'The quick brown fox jumps' # adglvyz
    missingPangram(str)