import sys
import heapq
import itertools

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLabel, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
)
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import QRectF, Qt, QTimer

CELL_SIZE = 25
GRID_ROWS = 20
GRID_COLS = 30

class Cell(QGraphicsRectItem):
    def __init__(self, row, col):
        super().__init__(0, 0, CELL_SIZE, CELL_SIZE)
        self.row = row
        self.col = col

        self.setPos(col * CELL_SIZE, row * CELL_SIZE)
        self.setBrush(QColor('white'))
        self.setPen(QColor('black'))
        self.type = 'empty'
        self.text_item = QGraphicsSimpleTextItem("", self)
        self.text_item.setFont(QFont("Arial", 8))
        self.text_item.setBrush(QColor("black"))
        self.text_item.setPos(3, 3)
        self.setAcceptHoverEvents(True)
        self.hover_text = None
    def set_type(self, cell_type):
        color_map = {
            'empty': 'white',
            'wall': 'black',
            'start': 'green',
            'goal': 'red',
            'visited': 'lightblue',
            'path': 'yellow'
        }
        self.type = cell_type
        self.setBrush(QColor(color_map[cell_type]))
        if cell_type not in ('path', 'visited'):
            self.text_item.setText("")
        if self.hover_text:
            self.scene().removeItem(self.hover_text)
            self.hover_text = None

    def set_step_label(self, text):
        self.text_item.setText(str(text))

    def hoverEnterEvent(self, event):
        if self.type == 'path' and self.text_item.text():
            self.hover_text = QGraphicsSimpleTextItem(f"Step: {self.text_item.text()}", self)
            self.hover_text.setFont(QFont("Arial", 10))
            self.hover_text.setBrush(QColor("blue"))
            self.hover_text.setZValue(1)
            self.hover_text.setPos(self.scenePos().x(), self.scenePos().y() - 20)
            self.scene().addItem(self.hover_text)
        super().hoverEnterEvent(event)
    def hoverLeaveEvent(self, event):
        if self.hover_text:
            self.scene().removeItem(self.hover_text)
            self.hover_text = None
        super().hoverLeaveEvent(event)

class Grid:
    def __init__(self, scene):
        self.scene = scene
        self.cells = [[Cell(r, c) for c in range(GRID_COLS)] for r in range(GRID_ROWS)]
        for row in self.cells:
            for cell in row:
                self.scene.addItem(cell)
        self.start = None
        self.goal = None

    def reset(self):
        for row in self.cells:
            for cell in row:
                if cell.type in ('visited', 'path'):
                    cell.set_type('empty')

    def clear_all(self):
        for row in self.cells:
            for cell in row:
                cell.set_type('empty')
                cell.text_item.setText("")
        self.start = None
        self.goal = None

    def neighbors(self, cell):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []
        for dr, dc in directions:
            r, c = cell.row + dr, cell.col + dc
            if 0 <= r < GRID_ROWS and 0 <= c < GRID_COLS:
                neighbor = self.cells[r][c]
                if neighbor.type != 'wall':
                    result.append(neighbor)
        return result

def heuristic(cell1, cell2):
    return abs(cell1.row - cell2.row) + abs(cell1.col - cell2.col)

def astar(grid):
    start = grid.start
    goal = grid.goal
    
    counter = itertools.count()

    open_set = []
    heapq.heappush(open_set, (0, next(counter), start))
    
    came_from = {}
    cost_so_far = {start: 0}
    
    visited_order = []

    while open_set:
        current = heapq.heappop(open_set)[2]

        if current == goal:
            break

        for neighbor in grid.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, next(counter), neighbor))
                came_from[neighbor] = current
                visited_order.append(neighbor)
                
    return came_from, visited_order

def greedy_best_first(grid):
    start = grid.start
    goal = grid.goal
    
    open_set = []
    counter = itertools.count()

    heapq.heappush(open_set, (heuristic(start, goal), next(counter), start))
    
    came_from = {}
    visited_order = []

    while open_set:
        current = heapq.heappop(open_set)[2]

        if current == goal:
            break

        for neighbor in grid.neighbors(current):
            if neighbor not in visited_order and neighbor not in [item[2] for item in open_set]: # This line needs to be handled carefully if 'open_set' can contain duplicates for the same neighbor. A set of visited/in-open-set nodes would be more efficient.
                heapq.heappush(open_set, (heuristic(neighbor, goal), next(counter), neighbor))
                came_from[neighbor] = current
                visited_order.append(neighbor)
    return came_from, visited_order

class PathfindingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Pathfinding Visualizer")
        self.scene = QGraphicsScene()
        self.grid = Grid(self.scene)

        self.view = QGraphicsView(self.scene)
        self.combo = QComboBox()
        self.combo.addItems(["A*", "Greedy Best-First"])
        self.run_btn = QPushButton("Run")
        self.run_btn.clicked.connect(self.run_search)
        self.clear_btn = QPushButton("Clear Grid")
        self.clear_btn.clicked.connect(self.clear_grid)
        self.step_label = QLabel("Steps: 0")

        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("Algorithm:"))
        top_bar.addWidget(self.combo)
        top_bar.addWidget(self.run_btn)
        top_bar.addWidget(self.clear_btn)
        top_bar.addWidget(self.step_label)

        layout = QVBoxLayout()
        layout.addLayout(top_bar)
        layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.view.setFixedSize(GRID_COLS * CELL_SIZE + 2, GRID_ROWS * CELL_SIZE + 2)
        self.view.setRenderHints(self.view.renderHints()) 

        self.view.setMouseTracking(True)
        self.view.viewport().installEventFilter(self)
        self.mode = 'wall'

        self.timer = QTimer()
        self.timer.timeout.connect(self.step_visualization)
        self.search_steps = []
        self.path = []
        self.step_counter = 0

    def eventFilter(self, source, event):
        if event.type() == event.Type.MouseButtonPress:
            pos = self.view.mapToScene(event.pos())
            col = int(pos.x() // CELL_SIZE)
            row = int(pos.y() // CELL_SIZE)
            if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
                cell = self.grid.cells[row][col]
                if self.grid.start is None:
                    cell.set_type('start')
                    self.grid.start = cell
                elif self.grid.goal is None:
                    cell.set_type('goal')
                    self.grid.goal = cell
                elif cell.type == 'empty':
                    cell.set_type('wall')
                elif cell.type == 'wall':
                    cell.set_type('empty')
        return super().eventFilter(source, event)

    def run_search(self):
        self.grid.reset()
        algorithm = self.combo.currentText()
        if algorithm == "A*":
            came_from, steps = astar(self.grid)
        elif algorithm == "Greedy Best-First":
            came_from, steps = greedy_best_first(self.grid)
        else:
            return

        self.search_steps = steps
        self.reconstruct_path(came_from)
        self.step_counter = 0
        self.step_label.setText("Steps: 0")
        self.timer.start(50)

    def clear_grid(self):
        self.grid.clear_all()
        self.step_label.setText("Steps: 0")
        self.search_steps = []
        self.path = []
        self.step_counter = 0
        self.timer.stop()

    def step_visualization(self):
        if self.search_steps:
            cell = self.search_steps.pop(0)
            if cell not in (self.grid.start, self.grid.goal):
                cell.set_type('visited')
            self.step_counter += 1
            self.step_label.setText(f"Steps: {self.step_counter}")

            # Mark second and third top choices (if any)
            if len(self.search_steps) > 1:
                second = self.search_steps[0]
                if second not in (self.grid.start, self.grid.goal):
                    second.setBrush(QColor("orange")) # second best choice
            if len(self.search_steps) > 2:
                third = self.search_steps[1]
                if third not in (self.grid.start, self.grid.goal):
                    third.setBrush(QColor("pink")) # third best choice

        elif self.path:
            cell = self.path.pop(0)
            if cell not in (self.grid.start, self.grid.goal):
                cell.set_type('path')
            self.step_counter += 1 # <-- Continue counting from last step
            self.step_label.setText(f"Steps: {self.step_counter}")

        else:
            self.timer.stop()

    def reconstruct_path(self, came_from):
        current = self.grid.goal
        while current != self.grid.start:
            current = came_from.get(current)
            if current is None:
                break
            self.path.insert(0, current)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PathfindingApp()
    window.show()
    sys.exit(app.exec())