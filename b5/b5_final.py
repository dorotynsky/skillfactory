print('Welcome to the game Tic-tac-toe')
print('You know how it works. Good luck!')
grid = [['-' for j in range(3)] for i in range(3)]


def print_current_grid():
    print('________________________')
    print('This is the current grid')
    for row in grid:
        print(row)
    print('________________________')
    print()


print_current_grid()


def is_stalemate():
    for row in grid:
        for el in row:
            if el == '-':
                return False
    print('Nobody wins')
    return True


def who_is_winner(elements):
    if elements[0] == 'X' and len(elements) == elements.count(elements[0]):
        print('The winner is X-player')
        return True
    elif elements[0] == '0' and len(elements) == elements.count(elements[0]):
        print('The winner is 0-player')
        return True
    else:
        return False


def has_someone_win():
    line_1 = grid[0]
    line_2 = grid[1]
    line_3 = grid[2]
    column_1 = [col[0] for col in grid]
    column_2 = [col[1] for col in grid]
    column_3 = [col[2] for col in grid]
    main_diag = [grid[i][i] for i in range(len(grid))]
    anti_diag = [grid[i][-1 - i] for i in range(len(grid))]
    return who_is_winner(line_1) or who_is_winner(line_2) or who_is_winner(line_3) or who_is_winner(
        column_1) or who_is_winner(column_2) or who_is_winner(column_3) or who_is_winner(
        main_diag) or who_is_winner(anti_diag)


# ________________


while True:
    x_coordinates = list(map(int, (input
                                   ('''
Enter coordinates for X with a space between them (e.g. "1 1").
Coordinates for the cells:
0 0 | 0 1 | 0 2
1 0 | 1 1 | 1 2
2 0 | 2 1 | 2 2
''').split())))

    if grid[x_coordinates[0]][x_coordinates[1]] == '-':
        grid[x_coordinates[0]][x_coordinates[1]] = 'X'
    else:
        while grid[x_coordinates[0]][x_coordinates[1]] != '-':
            x_coordinates = list(map(int, (input('This cell already has X or 0. Enter another one: ').split())))
        grid[x_coordinates[0]][x_coordinates[1]] = 'X'

    print_current_grid()
    if has_someone_win():
        break
    if is_stalemate():
        break

    # ________________
    o_coordinates = list(map(int, (input
('''
Enter coordinates for 0 with a space between them (e.g. "1 1").
Coordinates for the cells:
0 0 | 0 1 | 0 2
1 0 | 1 1 | 1 2
2 0 | 2 1 | 2 2
''').split())))
    if grid[o_coordinates[0]][o_coordinates[1]] == '-':
        grid[o_coordinates[0]][o_coordinates[1]] = '0'
    else:
        while grid[o_coordinates[0]][o_coordinates[1]] != '-':
            o_coordinates = list(map(int, (input('This cell already has X or 0. Enter another one: ').split())))
        grid[o_coordinates[0]][o_coordinates[1]] = '0'

    print_current_grid()
    if has_someone_win():
        break
    if is_stalemate():
        break
