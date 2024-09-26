def counting(arr):
    positive_numbers = sum(1 for x in arr if x > 0)
    negative_numbers = sum(x for x in arr if x < 0)
    zero_numbers = sum(1 for x in arr if x == 0)
    
    positive_numbers - zero_numbers
    
    if arr == []:
        return []

    return [positive_numbers,negative_numbers]


print(counting([1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]))
print(counting([]))
