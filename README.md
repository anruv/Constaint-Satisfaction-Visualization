## Constraint Satisfaction Problem (CSP)

A **Constraint Satisfaction Problem (CSP)** is a mathematical problem defined by a set of variables, each with a domain of possible values, and a set of constraints that specify allowable combinations of values. CSPs are used in various fields such as artificial intelligence, scheduling, and resource allocation.

In the context of Sudoku, the CSP involves:
- **Variables**: Each cell in the 9x9 grid.
- **Domains**: Possible values for each cell (numbers 1-9).
- **Constraints**: Rules that must be satisfied (each number 1-9 must appear exactly once in each row, column, and 3x3 subgrid).

This project uses CSP techniques to solve Sudoku puzzles through backtracking and constraint propagation.

# Sudoku Solver and Generator

This project is a Sudoku solver and generator built using Python and Tkinter for visualization. The application allows you to generate a random Sudoku puzzle, solve it step-by-step with visualization, and reset the grid.

## Features

- **Generate Puzzle**: Create a random Sudoku puzzle.
- **Solve Puzzle**: Solve the Sudoku puzzle with step-by-step visualization.
- **Reset Grid**: Clear the grid to start over or input a new puzzle.

## Requirements

- **Python 3.x**
- **Tkinter**: Comes pre-installed with Python.

## Usage

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/sudoku-solver.git
   cd sudoku-solver
   ```

2. **Run the Script**:
   ```sh
   python sudoku.py
   ```

3. **Generate Puzzle**:
   - Click the "Generate" button to create a new Sudoku puzzle.

4. **Solve Puzzle**:
   - Click the "Solve" button to solve the puzzle with visualization.

5. **Reset Grid**:
   - Click the "Reset" button to clear the grid.
