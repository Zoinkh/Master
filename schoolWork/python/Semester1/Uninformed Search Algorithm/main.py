import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout,
    QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from collections import deque

ROWS, COLS = 10, 10


class MazeSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maze Solver (BFS, DFS, UCS, DLS, IDDFS)")
        self.resize(800, 750)

        self.buttons = {}
        self.state = {}
        self.start_pos = None
        self.goal_pos = None

        self.create_widgets()
        self.layout_widgets()
        self.build_grid()

    def create_widgets(self):
        self.grid_layout = QGridLayout()

        self.info_label = QLabel("Click to set Start, Goal, and Walls")
        self.info_label.setFont(QFont("Arial", 14))

        self.bfs_btn = QPushButton("Solve with BFS")
        self.dfs_btn = QPushButton("Solve with DFS")
        self.ucs_btn = QPushButton("Solve with UCS")
        self.dls_btn = QPushButton("Solve with DLS")
        self.iddfs_btn = QPushButton("Solve with IDDFS")
        self.clear_btn = QPushButton("Clear Grid")

        self.bfs_btn.clicked.connect(self.solve_bfs)
        self.dfs_btn.clicked.connect(self.solve_dfs)
        self.ucs_btn.clicked.connect(self.solve_ucs)
        self.dls_btn.clicked.connect(self.solve_dls)
        self.iddfs_btn.clicked.connect(self.solve_iddfs)
        self.clear_btn.clicked.connect(self.clear_grid)
    
    def layout_widgets(self):
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.bfs_btn)
        control_layout.addWidget(self.dfs_btn)
        control_layout.addWidget(self.ucs_btn)
        control_layout.addWidget(self.dls_btn)
        control_layout.addWidget(self.iddfs_btn)
        control_layout.addWidget(self.clear_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addLayout(self.grid_layout)
        layout.addLayout(control_layout)
        self.setLayout(layout)

    def build_grid(self):
        for i in range(ROWS):
            for j in range(COLS):
                btn = QPushButton("")
                btn.setFixedSize(40, 40)
                btn.setStyleSheet("background-color: white;")
                btn.setFont(QFont("Arial", 10, QFont.Weight.Bold))
                btn.clicked.connect(lambda _, x=i, y=j: self.toggle_cell(x, y))
                self.grid_layout.addWidget(btn, i, j)
                self.buttons[i, j] = btn
                self.state[i, j] = "empty"
    def toggle_cell(self, i, j):
        current = self.state[i, j]

        if self.start_pos is None:
            self.state[i, j] = "start"
            self.buttons[i, j].setStyleSheet("background-color: green;")
            self.buttons[i, j].setText("S")
            self.start_pos = (i, j)
        elif self.goal_pos is None and (i, j) != self.start_pos:
            self.state[i, j] = "goal"
            self.buttons[i, j].setStyleSheet("background-color: red;")
            self.buttons[i, j].setText("G")
            self.goal_pos = (i, j)
        elif current == "empty":
            self.state[i, j] = "wall"
            self.buttons[i, j].setStyleSheet("background-color: black;")
        elif current == "wall":
            self.state[i, j] = "empty"
            self.buttons[i, j].setStyleSheet("background-color: white;")

    def solve_bfs(self):
        self.solve(self.bfs)

    def solve_dfs(self):
        self.solve(self.dfs)

    def solve_ucs(self):
        self.solve(self.ucs)

    def solve_dls(self):
        self.solve(lambda s, g: self.dls(s, g, depth_limit=15))

    def solve_iddfs(self):
        self.solve(self.iddfs)

    def solve(self, algorithm):
        if not self.start_pos or not self.goal_pos:
            QMessageBox.warning(self, "Warning", "Please set both Start and Goal.")
            return

        self.clear_path_visuals()
        path = algorithm(self.start_pos, self.goal_pos)

        if path:
            for index, pos in enumerate(path[1:-1], start=1):
                self.buttons[pos].setStyleSheet("background-color: yellow;")
                self.buttons[pos].setText(str(index))
            self.info_label.setText(f"✅ Path Found! Steps: {len(path) - 1}")
        else:
            self.info_label.setText("❌ No Path Found.")
    def bfs(self, start, goal):
        queue = deque([([start], start)])  # Store (path, current_node)
        visited = set()

        while queue:
            path, (x, y) = queue.popleft()

            if (x, y) == goal:
                return path

            if (x, y) not in visited:
                visited.add((x, y))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < ROWS and 0 <= ny < COLS and self.state[nx, ny] != "wall"):
                        queue.append((path + [(nx, ny)], (nx, ny)))
        return None

    def dfs(self, start, goal):
        stack = [([start], start)]  # Store (path, current_node)
        visited = set()

        while stack:
            path, (x, y) = stack.pop()

            if (x, y) == goal:
                return path

            if (x, y) not in visited:
                visited.add((x, y))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < ROWS and 0 <= ny < COLS and self.state[nx, ny] != "wall"):
                        stack.append((path + [(nx, ny)], (nx, ny)))
        return None
    def ucs(self, start, goal):
        from queue import PriorityQueue
        pq = PriorityQueue()
        pq.put((0, [start]))
        visited = set()

        while not pq.empty():
            cost, path = pq.get()
            x, y = path[-1]

            if (x, y) == goal:
                return path

            if (x, y) not in visited:
                visited.add((x, y))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < ROWS and 0 <= ny < COLS and self.state[nx, ny] != "wall"):
                        pq.put((cost + 1, path + [(nx, ny)]))
        return None

    def dls(self, start, goal, depth_limit):
        return self.recursive_dls(start, goal, [], depth_limit)

    def recursive_dls(self, current, goal, path, depth):
        if current == goal:
            return path + [current]
        if depth == 0:
            return None

        x, y = current
        path.append(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < ROWS and 0 <= ny < COLS and self.state[nx, ny] != "wall" and (nx, ny) not in path):
                result = self.recursive_dls((nx, ny), goal, path.copy(), depth - 1)
                if result:
                    return result
        return None

    def iddfs(self, start, goal):
        for limit in range(1, ROWS * COLS):  # Max depth can be all cells
            result = self.dls(start, goal, limit)
            if result:
                return result
        return None
    def clear_path_visuals(self):
        for pos, btn in self.buttons.items():
            if self.state[pos] == "empty":
                btn.setStyleSheet("background-color: white;")
                btn.setText("")
            elif self.state[pos] == "start":
                btn.setText("S")
                btn.setStyleSheet("background-color: green;")
            elif self.state[pos] == "goal":
                btn.setText("G")
                btn.setStyleSheet("background-color: red;")

    def clear_grid(self):
        self.start_pos = None
        self.goal_pos = None
        for pos, btn in self.buttons.items():
            self.state[pos] = "empty"
            btn.setStyleSheet("background-color: white;")
            btn.setText("")
        self.info_label.setText("Click to set Start, Goal, and Walls")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MazeSolver()
    window.show()
    sys.exit(app.exec())