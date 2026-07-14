# SCT_SD_3

# Sudoku Solver using Python (Tkinter GUI)

## Overview

The Sudoku Solver is a Python-based desktop application developed using the Tkinter library. It allows users to enter an incomplete 9×9 Sudoku puzzle through a graphical user interface (GUI) and solves it automatically using the Backtracking Algorithm.

---

## Features

- User-friendly graphical interface
- Accepts user input for a 9×9 Sudoku puzzle
- Solves Sudoku puzzles automatically
- Uses the Backtracking Algorithm
- Clear button to reset the puzzle
- Displays an error message for invalid input
- Shows a message if no solution exists

---

## Technologies Used

- Python 3
- Tkinter (GUI Library)

---

## Algorithm Used

This project uses the **Backtracking Algorithm** to solve Sudoku puzzles.

### Steps:
1. Find an empty cell.
2. Try numbers from 1 to 9.
3. Check if the number is valid according to Sudoku rules.
4. If valid, place the number and continue recursively.
5. If no number works, backtrack and try another number.
6. Continue until the puzzle is completely solved.

---

## How to Run

1. Install Python 3 on your system.
2. Save the source code as `sudoku_solver.py`.
3. Open the project folder in Visual Studio Code or any Python IDE.
4. Run the following command:

---

## How to Use

1. Launch the application.
2. Enter the given Sudoku puzzle in the 9×9 grid.
3. Leave empty cells blank.
4. Click the **Solve** button.
5. The solved Sudoku puzzle will be displayed.
6. Click **Clear** to reset the grid.

---

## Future Enhancements

- Generate random Sudoku puzzles
- Add multiple difficulty levels
- Highlight invalid inputs
- Improve the graphical interface
- Save and load Sudoku puzzles

---

## Author

**Kolanu.Niharika Reddy**

---

## License

This project is created for educational and internship purposes.
