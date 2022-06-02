# List Less Than Ten

# List of  numbers
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

# assign input number as integer


for element in a:
    if element < 5:
        new_list.append(element)

print(new_list)
