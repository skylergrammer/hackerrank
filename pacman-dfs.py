import numpy as np

def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    grid = np.matrix([list(x) for x in grid])

    visited, stack = [], [(pacman_r, pacman_c)]
    moves = []
    food = False
    while len(stack) > 0 and not food:
        vertex = stack.pop()
        moves.append(vertex)

        if vertex in visited:
            continue

        visited.append(vertex)

        if vertex == (food_r, food_c):
            food = True
            continue

        row, col = vertex
        up_c = (row-1, col)
        left_c = (row, col-1)
        right_c = (row, col+1)
        down_c = (row+1, col)

        for each in [up_c, left_c, right_c, down_c]:
            rr, cc = each
            try:
                box = grid.item(each)
            except:
                box = None
            if box and box != '%' and each not in visited and each not in stack:
                stack.append(each)
    return visited


def main():

    grid = [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%------------%%------------%',
            '%-%%%%-%%%%%-%%-%%%%%-%%%%-%',
            '%.%%%%-%%%%%-%%-%%%%%-%%%%-%',
            '%-%%%%-%%%%%-%%-%%%%%-%%%%-%',
            '%--------------------------%',
            '%-%%%%-%%-%%%%%%%%-%%-%%%%-%',
            '%-%%%%-%%-%%%%%%%%-%%-%%%%-%',
            '%------%%----%%----%%------%',
            '%%%%%%-%%%%%-%%-%%%%%-%%%%%%',
            '%%%%%%-%%%%%-%%-%%%%%-%%%%%%',
            '%%%%%%-%------------%-%%%%%%',
            '%%%%%%-%-%%%%--%%%%-%-%%%%%%',
            '%--------%--------%--------%',
            '%%%%%%-%-%%%%%%%%%%-%-%%%%%%',
            '%%%%%%-%------------%-%%%%%%',
            '%%%%%%-%-%%%%%%%%%%-%-%%%%%%',
            '%------------%%------------%',
            '%-%%%%-%%%%%-%%-%%%%%-%%%%-%',
            '%-%%%%-%%%%%-%%-%%%%%-%%%%-%',
            '%---%%----------------%%---%',
            '%%%-%%-%%-%%%%%%%%-%%-%%-%%%',
            '%%%-%%-%%-%%%%%%%%-%%-%%-%%%',
            '%------%%----%%----%%------%',
            '%-%%%%%%%%%%-%%-%%%%%%%%%%-%',
            '%------------P-------------%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            ]
    pacman_r, pacman_c = 25, 13
    food_r, food_c = 3, 1
    r, c = 27, 28
    visited = dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)

    print len(visited)
if __name__ == "__main__":
    main()
