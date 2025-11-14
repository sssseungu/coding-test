"""
Date: 25.10.14
스도쿠 (백트래킹, 구현)
URL
https://www.acmicpc.net/problem/2239
"""

if __name__ == "__main__":

    board = []
    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     lines = [list(line.strip("\n")) for line in f.readlines()]
    #     board = [[int(item) for item in row] for row in lines]

    for _ in range(9):
        board.append(list(map(int, input().strip())))

    def solve_sudoku(board):

        empty_cells = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    empty_cells.append((row, col))

        def is_valid(cur_row, cur_col, num):

            for i in range(9):
                if board[cur_row][i] == num or board[i][cur_col] == num:
                    return False

            block_row, block_col = (cur_row // 3) * 3, (cur_col // 3) * 3

            for row in range(block_row, block_row + 3):
                for col in range(block_col, block_col + 3):
                    if board[row][col] == num:
                        return False

            return True

        def backtrack(idx):

            if idx == len(empty_cells):
                return True

            empty_row, empty_col = empty_cells[idx]

            for num in range(1, 10):
                if is_valid(empty_row, empty_col, num):
                    board[empty_row][empty_col] = num

                    if backtrack(idx + 1):
                        return True

                    board[empty_row][empty_col] = 0

            return False

        backtrack(0)

        for row in board:
            print("".join(map(str, row)))

    solve_sudoku(board)
