def table_game(table):
    A = table[0][0] + table[0][1] + table[1][0] + table[1][1] 
    B = table[0][1] + table[0][2] + table[1][1] + table[1][2] 
    C = table[1][0] + table[1][1] + table[2][0] + table[2][1]
    D = table[1][1] + table[1][2] + table[2][1] + table[2][2]
    


    if (A + B) != (C + D):
        return [-1]
    

    return [A, B, C, D]

print(table_game([
[3,7,4],
[5,16,11],
[2,9,7]

]))
