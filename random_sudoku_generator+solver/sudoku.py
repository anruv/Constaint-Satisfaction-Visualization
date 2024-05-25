import tkinter as tk
from random import sample

class SudokuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.create_widgets()
        self.generate_puzzle()

    def create_widgets(self):
        self.entries = [[tk.Entry(self.master, width=3, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)
        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        self.solve_button.grid(row=9, column=0, columnspan=9)

    def generate_puzzle(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_diagonal()
        self.fill_remaining(0, 3)
        self.remove_digits()
        self.update_entries()

    def fill_diagonal(self):
        for i in range(0, 9, 3):
            self.fill_box(i, i)

    def fill_box(self, row, col):
        num = sample(range(1, 10), 9)
        for i in range(3):
            for j in range(3):
                self.grid[row+i][col+j] = num.pop()

    def check_if_safe(self, i, j, num):
        return (self.not_in_row(i, num) and
                self.not_in_col(j, num) and
                self.not_in_box(i-i%3, j-j%3, num))

    def not_in_row(self, i, num):
        for j in range(9):
            if self.grid[i][j] == num:
                return False
        return True

    def not_in_col(self, j, num):
        for i in range(9):
            if self.grid[i][j] == num:
                return False
        return True

    def not_in_box(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.grid[row+i][col+j] == num:
                    return False
        return True

    def fill_remaining(self, i, j):
        if j >= 9 and i < 9-1:
            i += 1
            j = 0
        if i >= 9 and j >= 9:
            return True
        if i < 3:
            if j < 3:
                j = 3
        elif i < 9-3:
            if j == int(i/3)*3:
                j += 3
        else:
            if j == 9-3:
                i += 1
                j = 0
                if i >= 9:
                    return True
        for num in range(1, 10):
            if self.check_if_safe(i, j, num):
                self.grid[i][j] = num
                if self.fill_remaining(i, j+1):
                    return True
                self.grid[i][j] = 0
        return False

    def remove_digits(self):
        count = 30
        while count != 0:
            cell_id = sample(range(81), 1)[0]
            i = cell_id // 9
            j = cell_id % 9
            if self.grid[i][j] != 0:
                count -= 1
                self.grid[i][j] = 0

    def update_entries(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
                    self.entries[i][j].config(state='readonly')
                else:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].config(state='normal')

    def solve(self):
        self.solve_sudoku()
        self.update_entries()

    def solve_sudoku(self):
        empty = self.find_empty_location()
        if not empty:
            return True
        i, j = empty
        for num in range(1, 10):
            if self.check_if_safe(i, j, num):
                self.grid[i][j] = num
                if self.solve_sudoku():
                    return True
                self.grid[i][j] = 0
        return False

    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def reset_grid(self):
        self.generate_puzzle()
        self.update_entries()

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
