import numpy as np

def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    grid = np.matrix([list(x) for x in grid])

    visited, stack = [], [(pacman_r, pacman_c)]
    moves = []
    vertex = (pacman_r, pacman_c)
    while len(stack) > 0 and vertex != (food_r, food_c):
        vertex = stack.pop()
        if vertex in visited:
            continue

        visited.append(vertex)
        moves.append(vertex)

        row, col = vertex
        up_c = (row-1, col)
        left_c = (row, col-1)
        right_c = (row, col+1)
        down_c = (row+1, col)

        for each in [up_c, left_c, right_c, down_c]:
            xx, yy = each
            try:
                box = grid.item(each)
                if 0 <= xx <= r-1 and 0 <= yy <= c-1 and box != '%':
                    stack.append(each)
            except:
                continue
                
    return moves


def main():

    grid = [
            '%%%%%%%%%%%%%%%%%%%%',
            '%--------------%---%',
            '%-%%-%%-%%-%%-%%-%-%',
            '%--------P-------%-%',
            '%%%%%%%%%%%%%%%%%%-%',
            '%.-----------------%',
            '%%%%%%%%%%%%%%%%%%%%'
            ]
    pacman_r, pacman_c = 3,9
    food_r, food_c = 5, 1
    r, c = 7, 20
    moves = dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)

    print len(moves)
    for each in moves:
        rr, cc = each
        print rr, cc

    print len(moves)-1
    for each in moves:
        rr, cc = each
        print rr, cc
if __name__ == "__main__":
    main()
