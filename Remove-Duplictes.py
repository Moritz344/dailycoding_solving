def removeDuplicates(nums):

    unique_num = []
    
    for num in nums: # Iteration über die Liste
        if num not in unique_num: # Wenn num nicht in der Liste ist wird sie hinzgefügt
            unique_num.append(num)

    nums[:] = unique_num # Aktualisiert und Kopiert die Liste.

data = [1,1,2,2,4,5]
removeDuplicates(data)
print(data)
