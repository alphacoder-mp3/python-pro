items = ["apple", "banana", "orange", "pear", "grape", "kiwi", "peach", "plum",  "orange",]

unique_items =  set(items)
# print(unique_items)
# print("Number of unique items:", len(unique_items))
# print("Number of items:", len(items))
# print("Number of duplicate items:", len(items) - len(unique_items))
# print("Duplicate items are:")
# for i in unique_items:
#     if items.count(i) > 1:
#         print(i)
# What will be the output of the following code:


for item in items:
    if item in unique_items:
        print("Duplicate item:", item)
        break;
    unique_items.add(item)
# Options
# A. Duplicate item: orange
# B. Duplicate item: orange
# C. Duplicate item: apple
# D. Duplicate item: apple
# E. Duplicate item: apple
# F. Duplicate item: apple
# G. Duplicate item: apple
# H. Duplicate item: apple
