# Data_Type

# 1. Integer: A whole number can be positive, negative or O
integer_list = [1000,-65,0]
print(integer_list)

# 2. Real Number: The union of both rational and irrational numbers
real_num_list = [157.93, -125.3, 51., -.62]
print(real_num_list)

# 2-1. Scientific Notation: A number as a factor multiplied by a power of 10
scientific_notation_list = [1e9, 75.25e1, 5631e-3]
print(scientific_notation_list)

# 2-2. Floating Point Error
floating_point_error = 0.3 + 0.6
print(floating_point_error)

if floating_point_error == 0.9:
    print('True')
else:
    print('False')

print(round(floating_point_error,4))
if round(floating_point_error,4) == 0.9:
    print('True')
else:
    print('False')

# 3. Numeric Operators
a = 7
b = 3

# Division
print(a / b)

# Quotient
print(a // b)

# Remainder
print(a % b)

# Power
print(a ** b)

# Square Root
print(a ** 0.5)

# 4. List:  A number of items in an ordered or unordered structure
list_list = [1,2,3,4,5,6,7,8,9]
print(list_list)

empty_list = []
print(empty_list)

# Reset List
n = 10
reset_list = [0] * n
print(reset_list)

# 4.1 Indexing & Slicing

# Last Element of The List
print(list_list[-1])

# Changing the Element Value
list_list[3] = 7
print(list_list)