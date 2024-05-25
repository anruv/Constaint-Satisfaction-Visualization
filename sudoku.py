import tkinter as tk
from tkinter import messagebox
import random

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Visualization")
        self.create_grid()
        self.create_buttons()
        self.solved = False
        self.running = False

    def create_grid(self):
        self.cells = {}
        self.entries = []

        for row in range(9):
            row_entries = []
            for col in range(9):
                cell = tk.Entry(self.root, width=2, font=('Arial', 24), justify='center')
                cell.grid(row=row, column=col, padx=(5 if col % 3 == 0 else 1), pady=(5 if row % 3 == 0 else 1), ipadx=10, ipady=10)
                self.cells[(row, col)] = cell
                row_entries.append(cell)
            self.entries.append(row_entries)

        for i in range(9):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=0, columnspan=3)
        
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_grid)
        reset_button.grid(row=9, column=3, columnspan=3)
        
        generate_button = tk.Button(self.root, text="Generate", command=self.generate_puzzle)
        generate_button.grid(row=9, column=6, columnspan=3)

    def check_constraints(self, event=None):
        grid = self.get_grid()
        conflicts = self.apply_constraints(grid)
        self.highlight_conflicts(conflicts)

    def get_grid(self):
        grid = []
        for row in range(9):
            grid_row = []
            for col in range(9):
                value = self.cells[(row, col)].get()
                grid_row.append(int(value) if value.isdigit() else None)
            grid.append(grid_row)
        return grid

    def apply_constraints(self, grid):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        conflicts = []

        for i in range(9):
            for j in range(9):
                value = grid[i][j]
                if value:
                    box_index = (i // 3) * 3 + (j // 3)
                    if value in rows[i] or value in cols[j] or value in boxes[box_index]:
                        conflicts.append((i, j))
                    else:
                        rows[i].add(value)
                        cols[j].add(value)
                        boxes[box_index].add(value)
        return conflicts

    def highlight_conflicts(self, conflicts):
        for (row, col) in self.cells:
            self.cells[(row, col)].config(bg='white')

        for (row, col) in conflicts:
            self.cells[(row, col)].config(bg='red')

    def solve_puzzle(self):
        grid = self.get_grid()
        self.solved = False
        self.running = True
        self.visualize_solve(grid)

    def visualize_solve(self, grid):
        if not self.running:
            return False

        empty_cell = self.find_empty_cell(grid)
        if not empty_cell:
            self.update_grid(grid)
            self.solved = True
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if not self.running:
                return False

            if self.is_safe(grid, row, col, num):
                grid[row][col] = num
                self.update_grid(grid)
                self.root.update()
                self.root.after(100)

                if self.visualize_solve(grid):
                    return True
                
                grid[row][col] = None
                self.update_grid(grid)
                self.root.update()
                self.root.after(100)

        return False

    def find_empty_cell(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] is None:
                    return (i, j)
        return None

    def is_safe(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False

        return True

    def update_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.cells[(row, col)].delete(0, tk.END)
                if grid[row][col] is not None:
                    self.cells[(row, col)].insert(0, str(grid[row][col]))

    def reset_grid(self):
        self.running = False
        for row in range(9):
            for col in range(9):
                self.cells[(row, col)].delete(0, tk.END)
                self.cells[(row, col)].config(bg='white')

    def generate_puzzle(self):
        self.reset_grid()
        board = [[None for _ in range(9)] for _ in range(9)]
        self.generate_full_board(board)
        self.remove_cells(board)
        self.update_grid(board)

    def generate_full_board(self, board):
        numbers = list(range(1, 10))
        for row in range(9):
            for col in range(9):
                if board[row][col] is None:
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_safe(board, row, col, num):
                            board[row][col] = num
                            if self.generate_full_board(board):
                                return True
                            board[row][col] = None
                    return False
        return True

    def remove_cells(self, board, num_cells_to_remove=45):
        count = 0
        while count < num_cells_to_remove:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] is not None:
                board[row][col] = None
                count += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
