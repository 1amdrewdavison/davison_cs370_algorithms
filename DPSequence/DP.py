def traverse_table(table: list, s1: str, s2: str) -> tuple[str, str]:
    s1_sol = []
    s2_sol = []
    i, j = len(table) - 1, len(table[0]) - 1

    while(i != 0 or j != 0):
        if (table[i - 1][j] + 2 == table[i][j]):
            s1_sol.append(s1[i - 1])
            s2_sol.append(' ')
            i = i - 1
        elif (table[i][j - 1] + 2 == table[i][j]):
            s1_sol.append(' ')
            s2_sol.append(s2[j - 1])
            j = j - 1
        elif (table[i - 1][j - 1] == table[i][j] or table[i - 1][j - 1] + 1 == table[i][j]):
            s1_sol.append(s1[i - 1])
            s2_sol.append(s2[j - 1])
            i = i - 1
            j = j - 1
      
    sol1 = ''.join(s1_sol)
    sol2 = ''.join(s2_sol)
    return (sol1[::-1], sol2[::-1])

def fill_table_recursively(row: int, col: int, s1: str, s2: str, table: list) -> int:
    if (table[row][col] != -1):
        return table[row][col]
    elif (row == 0 and col == 0):
        table[row][col] = 0
    elif (row == 0):
        table[row][col] = 2 * col
    elif (col == 0):
        table[row][col] = 2 * row
    else:
        if (s1[row - 1] == s2[col - 1]):
            penalty = 0
        else:
            penalty = 1

        table[row][col] = min(fill_table_recursively(row - 1, col - 1, s1, s2, table) + penalty, fill_table_recursively(row - 1, col, s1, s2, table) + 2, fill_table_recursively(row, col - 1, s1, s2, table) + 2)
    
    return table[row][col]

def align_sequences_recursive(s1: str, s2: str) -> tuple[str, str]:
    match_table = []

    for i in range(len(s1) + 1):
        match_table.append([])
        for j in range(len(s2) + 1):
            match_table[i].append(-1)

    fill_table_recursively(len(s1), len(s2), s1, s2, match_table)
    
    return traverse_table(match_table, s1, s2)

s1 = "AACAGTTACC"
s2 = "TAAGGTCA"

aligned_sequence1, aligned_sequence2 = align_sequences_recursive(s1, s2)
print(aligned_sequence1)
print(aligned_sequence2)