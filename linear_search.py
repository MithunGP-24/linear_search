def linear_search(arr, item):
    for index in range(len(arr)):
        if arr[index] == item:
            return index  # Return index if item is found
    return -1  # Return -1 if item is not found

# Input list elements
list_ = []  # Use a descriptive variable name
n = int(input("Enter the number of elements: "))
for j in range(n):
    i = int(input("Enter element: "))
    list_.append(i)

# Input the target item to search for
target = int(input("Enter the element to search: "))

# Perform linear search
result = linear_search(list_, target)

# Display the result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
