# For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.


def sum_of_square(array):
        return sum(x * x for x in array)


for i in range(0,999):
    for z in range(0,1):
        print(sum_of_square([i,z]))

