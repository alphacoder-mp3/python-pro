num = int(input("Enter a number: "))

i = 1
temp = num

while  i < temp :    
    num = num * (temp - i)
    i = i + 1
    
print("factorial is:", num)