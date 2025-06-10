import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator # Import QIntValidator from QtGui
import random
import copy

class SudokuSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku Solver with PyQt6")
        self.setGeometry(100, 100, 450, 540)

        self.main_layout = QVBoxLayout()

        # Title and instruction
        title_label = QLabel("Sudoku Solver")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instruction_label = QLabel("Fill the Sudoku grid with digits 1-9. Use 'Get Hint' up to 5 times per puzzle.")
        instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addWidget(title_label)
        self.main_layout.addWidget(instruction_label)

        self.grid_layout = QGridLayout()
        self.cells = [[QLineEdit(self) for _ in range(9)] for _ in range(9)]
        self.hint_count = 0
        self.max_hints = 81
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.setFixedSize(40, 40)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setMaxLength(1)
                cell.setStyleSheet("font-size: 16px;")
                # Use QIntValidator directly as it's now imported
                cell.setValidator(QIntValidator(1, 9, self)) 
                self.grid_layout.addWidget(cell, row, col)

        self.hint_button = QPushButton(f"Get Hint ({self.max_hints - self.hint_count} left)")
        self.hint_button.clicked.connect(self.provide_hint)

        self.solve_button = QPushButton("Solve Sudoku")
        self.solve_button.clicked.connect(self.solve)

        self.clear_button = QPushButton("Clear Board")
        self.clear_button.clicked.connect(self.clear_board)

        self.new_button = QPushButton("New Game")
        self.new_button.clicked.connect(self.start_new_game)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.solve_button)
        button_layout.addWidget(self.hint_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.new_button)

        self.main_layout.addLayout(self.grid_layout)
        self.main_layout.addLayout(button_layout)
        self.setLayout(self.main_layout)

    def get_board(self):
        board = []
        for row in range(9):
            board_row = []
            for col in range(9):
                text = self.cells[row][col].text()
                try:
                    if text == '':
                        board_row.append(0)
                    elif text.isdigit():
                        num = int(text)
                        if 1 <= num <= 9:
                            board_row.append(num)
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                except ValueError:
                    QMessageBox.warning(self, "Invalid Input", f"Cell ({row+1}, {col+1}) contains an invalid entry.")
                    return None
            board.append(board_row)
        return board

    def set_board(self, board):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].setText(str(board[row][col]) if board[row][col] != 0 else "")

    def clear_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].clear()
                self.cells[row][col].setStyleSheet("font-size: 16px;")
        self.hint_count = 0
        self.hint_button.setText(f"Get Hint ({self.max_hints - self.hint_count} left)")

    def start_new_game(self):
        self.clear_board()
        QMessageBox.information(self, "New Game", "New game started. Board cleared.")

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve_sudoku(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve_sudoku(board):
                                return True
                            board[row][col] = 0  # Backtrack
                    return False  # No valid number found for this cell
        return True  # All cells filled

    def solve(self):
        board = self.get_board()
        if board is None:
            return

        if self.solve_sudoku(board):
            self.set_board(board)
        else:
            QMessageBox.warning(self, "No Solution", "No valid solution exists for the current Sudoku puzzle.")

    def provide_hint(self):
        if self.hint_count >= self.max_hints:
            QMessageBox.information(self, "Hint Limit", "You have used all 81 hints.")
            return

        current_board = self.get_board()
        if current_board is None:
            return

        solved_board = copy.deepcopy(current_board)

        if not self.solve_sudoku(solved_board):
            QMessageBox.warning(self, "No Solution", "No valid solution exists for the current puzzle.")
            return

        hint_candidates = [(r, c) for r in range(9) for c in range(9)
                           if current_board[r][c] == 0 and solved_board[r][c] != 0]

        if not hint_candidates:
            QMessageBox.information(self, "Hint", "No empty cells available for hints.")
            return

        row, col = random.choice(hint_candidates)
        hint_value = solved_board[row][col]
        self.cells[row][col].setText(str(hint_value))
        self.cells[row][col].setStyleSheet("font-size: 16px; color: blue;")
        self.hint_count += 1
        self.hint_button.setText(f"Get Hint ({self.max_hints - self.hint_count} left)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SudokuSolver()
    window.show()
    sys.exit(app.exec())