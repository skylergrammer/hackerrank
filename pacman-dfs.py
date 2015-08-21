import numpy as np

def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    grid = np.matrix([list(x) for x in grid])
    col_num = pacman_c
    row_num = pacman_r
    visited = []

    contents = grid.item(row_num, col_num)

    n = 0
    while contents != '.' and n < 20:
        contents = grid.item(row_num, col_num)
        visited.append((row_num, col_num))

        if row_num-1 >= 0:
            contents_up = grid.item(row_num-1, col_num)
        else:
            contents_up = None

        if col_num-1 >= 0:
            contents_left = grid.item(row_num, col_num-1)
        else:
            contents_left = None

        if col_num+1 <= c-1:
            contents_right = grid.item(row_num, col_num+1)
        else:
            contents_right = None

        if row_num+1 <= r-1:
            contents_down = grid.item(row_num-1, col_num)
        else:
            contents_down = None

        if contents_up and contents_up == '-' and (row_num-1, col_num) not in visited:
            row_num -= 1
        elif contents_left and contents_left == '-' and (row_num, col_num-1) not in visited:
            col_num -= 1
        elif contents_right and contents_right == '-' and (row_num+1, col_num) not in visited:
            row_num += 1
        elif contents_down and contents_down == '-' and (row_num, col_num-1) not in visited:
            col_num += 1

        n+=1

        print row_num, col_num

    return

def main():

    grid = ['%%%%%%%%%%%%%%%%%%%%',
            '%--------------%---%',
            '%-%%-%%-%%-%%-%%-%-%',
            '%--------P-------%-%',
            '%%%%%%%%%%%%%%%%%%-%',
            '%.-----------------%',
            '%%%%%%%%%%%%%%%%%%%%']
    pacman_r, pacman_c = 3, 9
    food_c, food_r = 5, 1
    r, c = 7, 20
    new_grid = dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)

if __name__ == "__main__":
    main()
