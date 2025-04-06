from array import array


arr = array('i', [1, 2, 3, 4])

print(arr)
print(arr[2])

arr.insert(0, 6)
print(arr)

arr.pop()
print(arr)

# Serach is similar to a for loop on this object
print(type(arr))
