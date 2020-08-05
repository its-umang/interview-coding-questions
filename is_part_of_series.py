def is_part_of_series(n): 
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return 0     
    elif n == 1: 
        return 1     
    else: 
        return 3 * is_part_of_series(n - 1) - 2 * is_part_of_series(n - 2) 
 
input_string = input("Enter a list: ")
userList = input_string.split() 
print("user list is ", userList) 
a = 0 
while (is_part_of_series(a) != int(userList[0])): 
    a = a + 1 
length = len(userList) 
for i in range(length): 
    if is_part_of_series(a) == int(userList[i]): 
        a = a + 1     
    else: 
        print('Sad! Not Part of the Series') 
        break
print("Oh! Yay Part of the Series")