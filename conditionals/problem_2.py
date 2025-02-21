age = int(input("Enter your age: "))
day=input("Enter a weekday: ")


price = 12 if age >= 18 else 8

if day == 'wednesday':  price -= 2

print('you have to pay:', price)

# if(day == 'wednesday'):
#     if(age>=18):
#         print("You have to pay $10")
#     if(age<18): 
#         print("You have to pay $6")
# else:
#     if(age>=18):
#         print("You have to pay $12")
#     if(age<18): 
#         print("You have to pay $8")