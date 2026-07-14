import tkinter as tk
from tkinter import messagebox

# Check if a number is valid
def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


# Solve Sudoku using Backtracking
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0
                return False
    return True


# Read values from GUI
def solve_sudoku():
    board = []

    try:
        for i in range(9):
            row = []
            for j in range(9):
                value = entries[i][j].get()
                if value == "":
                    row.append(0)
                else:
                    row.append(int(value))
            board.append(row)

        if solve(board):
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showinfo("Result", "No Solution Exists!")

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers from 1 to 9 only.")


# Clear all cells
def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)


# GUI
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("420x500")

entries = []

for i in range(9):
    row = []
    for j in range(9):
        e = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        row.append(e)
    entries.append(row)

solve_btn = tk.Button(root, text="Solve", command=solve_sudoku,
                      font=("Arial", 14), bg="green", fg="white")
solve_btn.grid(row=10, column=2, columnspan=2, pady=20)

clear_btn = tk.Button(root, text="Clear", command=clear_board,
                      font=("Arial", 14), bg="red", fg="white")
clear_btn.grid(row=10, column=5, columnspan=2, pady=20)

root.mainloop()