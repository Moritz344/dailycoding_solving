#Principal Diagonal -- The principal diagonal in a matrix identifies those elements of the matrix running from North-West to South-East.

#Secondary Diagonal -- the secondary diagonal of a matrix identifies those elements of the matrix running from North-East to South-West.

#For example:

#matrix:             [1, 2, 3]
#                    [4, 5, 6]
#                    [7, 8, 9]

#principal diagonal: [1, 5, 9]
#secondary diagonal: [3, 5, 7]

def diagonal(matrix):
        row1 = matrix[0] 
        row2 = matrix[1]
        row3 = matrix[2]
        
        prinicpal_diagonal_sum = row1[0] + row2[1] + row3[2] 
        
        secondary_diagonal_sum = row1[2] + row2[1] + row3[0] 

        if prinicpal_diagonal_sum > secondary_diagonal_sum:
            return "Principal Diagonal win!"
        else:
            return "Secondary Diagonal win!"


print(diagonal([ [2,2,2],
                 [4,2,6],
                 [8,8,2] ]))


