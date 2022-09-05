import numpy as np

f = open('input17.txt')
inp_ = f.read().split('\n')
board = np.array([list(x.replace('.', '0').replace('#', '1')) for x in inp_]).astype(int)

# part 1 - took 3 days to figure out that the old board is updated separately from the new one so I need two copies


def _3d_part1(board, cycles):
    board = board.reshape((1, board.shape[0], board.shape[1]))

    total_active_cubes = np.sum(board)
    for _ in range(cycles):
        board_copy = np.pad(board, pad_width=1)
        board = board_copy.copy()
        for layer in range(board_copy.shape[0]):
            for row in range(board_copy.shape[1]):
                for cube in range(board_copy.shape[2]):
                    layer_min, row_min, cube_min = max(0, layer-1), max(0, row-1), max(0, cube-1)
                    layer_max, row_max, cube_max = min(board_copy.shape[0], layer+2), min(board_copy.shape[1], row+2), min(board_copy.shape[2], cube+2)
                    nearby_active_cubes = np.sum(board[layer_min:layer_max, row_min:row_max, cube_min:cube_max]) - \
                                          board[layer][row][cube]

                    if board[layer][row][cube] == 1 and not (nearby_active_cubes == 2 or nearby_active_cubes == 3):
                        board_copy[layer][row][cube] = 0
                        total_active_cubes -= 1
                    elif board[layer][row][cube] == 0 and nearby_active_cubes == 3:
                        board_copy[layer][row][cube] = 1
                        total_active_cubes += 1
        board = board_copy.copy()

    return np.sum(board_copy)


# print(_3d_part1(board, 6))


# part 2

def _4d_part1(board, cycles):
    board = board.reshape((1, 1, board.shape[0], board.shape[1]))

    total_active_cubes = np.sum(board)
    for _ in range(cycles):
        board_copy = np.pad(board, pad_width=1)
        board = board_copy.copy()
        for layer1 in range(board_copy.shape[0]):
            for layer2 in range(board_copy.shape[1]):
                for row in range(board_copy.shape[2]):
                    for cube in range(board_copy.shape[3]):
                        layer1_min, layer2_min, row_min, cube_min = max(0, layer1-1), max(0, layer2-1), max(0, row-1), max(0, cube-1)
                        layer1_max, layer2_max, row_max, cube_max = min(board_copy.shape[0], layer1+2), min(board_copy.shape[1], layer2+2), \
                                                                   min(board_copy.shape[2], row+2), min(board_copy.shape[3], cube+2)
                        nearby_active_cubes = np.sum(board[layer1_min:layer1_max, layer2_min:layer2_max, row_min:row_max, cube_min:cube_max]) - \
                                              board[layer1][layer2][row][cube]

                        if board[layer1][layer2][row][cube] == 1 and not (nearby_active_cubes == 2 or nearby_active_cubes == 3):
                            board_copy[layer1][layer2][row][cube] = 0
                            total_active_cubes -= 1
                        elif board[layer1][layer2][row][cube] == 0 and nearby_active_cubes == 3:
                            board_copy[layer1][layer2][row][cube] = 1
                            total_active_cubes += 1
        board = board_copy.copy()

    return np.sum(board_copy)


print(_4d_part1(board, 6))