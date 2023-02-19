grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# In grid[0][0] the first zero refers to the position of the list
# while the second zero refers to the position of the item in that list
ROW = len(grid)  # Number of rows
COL = len(grid[0])  # Number of columns

for y in range(COL):
    if y > 0:
        print()
    for x in range(ROW):
        print(grid[x][y], end=' ')
