

def reverse_string(str):
    s=''
    for i in str:
        s = i + s 
    return s

print(reverse_string(input('Enter a string ')))

# str = input('Enter a string')
# a=''
# for i in str:
#     a = i + a

# print(a)
