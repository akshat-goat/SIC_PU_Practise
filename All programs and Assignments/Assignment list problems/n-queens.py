def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(r, c):
        # Check row
        for col in range(c):
            if board[r][col] == 'Q':
                return False
        # Check upper diagonal
        for row, col in zip(range(r, -1, -1), range(c, -1, -1)):
            if board[row][col] == 'Q':
                return False
        # Check lower diagonal
        for row, col in zip(range(r, n), range(c, -1, -1)):
            if board[row][col] == 'Q':
                return False
        return True

    def backtrack(col):
        if col == n:
            solutions.append(["".join(row) for row in board])
            return

        for row in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.' # Backtrack

    backtrack(0)
    return solutions

def print_solutions(solutions):
    if not solutions:
        print("No solutions found.")
        return
    
    print(f"Found {len(solutions)} solutions:")
    for idx, sol in enumerate(solutions):
        print(f"--- Solution {idx + 1} ---")
        for row_str in sol:
            print(row_str)
        print("-" * 15)

if __name__ == "__main__":
    print("--- N-Queens Problem ---")
    n_val = int(input("Enter the size of the chessboard (N): "))
    if n_val <= 0:
        print("N must be a positive integer.")
    else:
        all_solutions = solve_n_queens(n_val)
        print_solutions(all_solutions)