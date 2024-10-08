def removeElement(nums,val):
    for i in range(len(nums)-1,-1,-1): # start stop step
        if nums[i] == val:
            nums.remove(val)




        

data = [3,2,2,3]
removeElement(data,2)
print(len(data))

exc = [2,2,2,4,4,6,7,8,9,9]
unique_num = []

for num in exc:
    if num not in unique_num:
        unique_num.append(num)
    print(unique_num)

for i in range(len(exc)-1,-1,-1):
    print(i,exc)

    if exc[i] == 3 or exc[i] == 2:
        del exc[i]

    print(exc)

