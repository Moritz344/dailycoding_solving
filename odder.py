def odd_one(arr):
    for index,number in enumerate(arr):
        if number % 2 != 0:
            return index


    return -1


print(odd_one([2,4,6,7]))

