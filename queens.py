def is_safe(board, row, col):
    # Check if no queen attacks this position
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n=8):
    solutions = []
    board = [-1] * n

    def backtrack(row=0):
        if row == n:
            solutions.append(board[:])  # copy solution
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # reset
    
    backtrack()
    return solutions

# Run for 8 queens
solutions = solve_n_queens(8)
print(f"Total solutions: {len(solutions)}")

# Print the first solution as a board
first = solutions[0]
for row in range(8):
    line = ""
    for col in range(8):
        line += "Q " if first[row] == col else ". "
    print(line)