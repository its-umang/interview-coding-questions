# Already given function substring
# word.find("abc") in python equivalent

# The idea is slicing
# From 3 we slice say x='wat', y='ermelon'
# such that s1 = xy & s2 = yx
# s1s1 = xyxy which contains s2(Just check) by one call of substring function

if __name__ == "__main__":
    s1 = 'watermelon'
    s2 = 'ermelonwat'
    # s2 = 'ermeonwatl' # False
    s1s1 = s1 + s1
    b = s1s1.find(s2)
    print(True if b!=-1 else False)