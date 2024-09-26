def print_array(arr):
    # Convert to string
    arr = [str(a) for a in arr]
    return ", ".join(arr)

data = [True,False,True]
print(print_array(data))
