import os
import random
import tkinter as tk


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 620
CELL_SIZE = 20
GRID_SIZE = WINDOW_WIDTH // CELL_SIZE

BG_COLOR = "#111111"
GRID_COLOR = "#2a2a2a"
PANEL_COLOR = "#1a1a1a"
SNAKE_COLOR = "#2ecc71"
SNAKE_HEAD_COLOR = "#1e8f4d"
FOOD_COLOR = "#ff5f6d"
TEXT_COLOR = "#f5f5f5"
ACCENT_COLOR = "#82c8ff"
DANGER_COLOR = "#ff5757"


def load_high_score():
    file_path = os.path.join(os.path.dirname(__file__), "snake_highscore.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            value = file.read().strip()
            return int(value) if value else 0
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    file_path = os.path.join(os.path.dirname(__file__), "snake_highscore.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(score))


def spawn_food(snake):
    free_cells = [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE) if (x, y) not in snake]
    if not free_cells:
        return None
    return random.choice(free_cells)


def create_initial_state():
    start_x = GRID_SIZE // 2
    start_y = GRID_SIZE // 2
    snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
    return {
        "snake": snake,
        "direction": (1, 0),
        "next_direction": (1, 0),
        "food": spawn_food(snake),
        "score": 0,
        "game_over": False,
        "paused": False,
        "speed": 140,
    }


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.high_score = load_high_score()
        self.state = create_initial_state()

        self.canvas = tk.Canvas(
            root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg=BG_COLOR,
            highlightthickness=0,
        )
        self.canvas.pack()

        self.status_label = self.canvas.create_text(
            25, 20, anchor="w", fill=TEXT_COLOR, font=("Arial", 18, "bold")
        )
        self.score_label = self.canvas.create_text(
            220, 20, anchor="w", fill=ACCENT_COLOR, font=("Arial", 18, "bold")
        )
        self.high_score_label = self.canvas.create_text(
            420, 20, anchor="w", fill=TEXT_COLOR, font=("Arial", 18, "bold")
        )
        self.info_label = self.canvas.create_text(
            170, 585, anchor="center", fill=TEXT_COLOR, font=("Arial", 12)
        )

        self.game_over_text = None
        self.pause_text = None

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.after(100, self.game_loop)

    def draw_board(self):
        self.canvas.delete("all")

        self.canvas.create_rectangle(0, 0, WINDOW_WIDTH, 52, fill=PANEL_COLOR, outline=PANEL_COLOR)

        self.canvas.itemconfig(self.status_label, text="Snake Game")
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.state['score']}")
        self.canvas.itemconfig(self.high_score_label, text=f"High Score: {self.high_score}")

        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            self.canvas.create_line(x, 52, x, WINDOW_HEIGHT, fill=GRID_COLOR)
        for y in range(52, WINDOW_HEIGHT, CELL_SIZE):
            self.canvas.create_line(0, y, WINDOW_WIDTH, y, fill=GRID_COLOR)

        food = self.state["food"]
        if food:
            fx, fy = food
            self.canvas.create_oval(
                fx * CELL_SIZE + 4,
                fy * CELL_SIZE + 54,
                fx * CELL_SIZE + CELL_SIZE - 4,
                fy * CELL_SIZE + CELL_SIZE + 52,
                fill=FOOD_COLOR,
                outline=FOOD_COLOR,
            )

        for index, segment in enumerate(self.state["snake"]):
            x, y = segment
            color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR
            self.canvas.create_rectangle(
                x * CELL_SIZE + 1,
                y * CELL_SIZE + 53,
                x * CELL_SIZE + CELL_SIZE - 1,
                y * CELL_SIZE + CELL_SIZE + 52,
                fill=color,
                outline=color,
                width=1
            )

        if index == 0:
            head_x = x * CELL_SIZE + CELL_SIZE // 2
            head_y = y * CELL_SIZE + CELL_SIZE // 2 + 52
            self.canvas.create_oval(head_x - 2, head_y - 2, head_x + 2, head_y + 2, fill="white")
            self.canvas.create_oval(head_x + 4, head_y - 2, head_x + 8, head_y + 2, fill="white")

        self.canvas.itemconfig(self.info_label, text="Use arrow keys or WASD • P = pause")

        if self.state["game_over"]:
            self.canvas.create_rectangle(100, 180, 500, 360, fill="black", outline="gray", stipple="gray50")
            self.canvas.create_text(300, 240, text="Game Over", fill=DANGER_COLOR, font=("Arial", 28, "bold"))
            self.canvas.create_text(300, 290, text="Press Enter to play again", fill=TEXT_COLOR, font=("Arial", 16))

        if self.state["paused"] and not self.state["game_over"]:
            self.canvas.create_text(300, 240, text="Paused", fill=ACCENT_COLOR, font=("Arial", 28, "bold"))

    def set_direction(self, new_dir):
        current = self.state["direction"]
        if new_dir == (0, -1) and current != (0, 1):
            self.state["next_direction"] = new_dir
        elif new_dir == (0, 1) and current != (0, -1):
            self.state["next_direction"] = new_dir
        elif new_dir == (-1, 0) and current != (1, 0):
            self.state["next_direction"] = new_dir
        elif new_dir == (1, 0) and current != (-1, 0):
            self.state["next_direction"] = new_dir

    def on_key_press(self, event):
        key = event.keysym.lower()

        if key in ("up", "w"):
            self.set_direction((0, -1))
        elif key in ("down", "s"):
            self.set_direction((0, 1))
        elif key in ("left", "a"):
            self.set_direction((-1, 0))
        elif key in ("right", "d"):
            self.set_direction((1, 0))
        elif key == "p":
            if not self.state["game_over"]:
                self.state["paused"] = not self.state["paused"]
        elif key == "return" and self.state["game_over"]:
            self.state = create_initial_state()
            self.high_score = load_high_score()

    def move_snake(self):
        if self.state["paused"] or self.state["game_over"]:
            return

        self.state["direction"] = self.state["next_direction"]
        head_x, head_y = self.state["snake"][0]
        dx, dy = self.state["direction"]
        new_head = (head_x + dx, head_y + dy)

        if (
            new_head[0] < 0
            or new_head[1] < 0
            or new_head[0] >= GRID_SIZE
            or new_head[1] >= GRID_SIZE
            or new_head in self.state["snake"]
        ):
            self.state["game_over"] = True
            return

        self.state["snake"].insert(0, new_head)

        if new_head == self.state["food"]:
            self.state["score"] += 1
            self.state["food"] = spawn_food(self.state["snake"])
            if self.state["food"] is None:
                self.state["game_over"] = True
                return
            self.state["speed"] = max(70, 140 - self.state["score"] * 5)
            if self.state["score"] > self.high_score:
                self.high_score = self.state["score"]
                save_high_score(self.high_score)
        else:
            self.state["snake"].pop()

    def game_loop(self):
        if not self.state["game_over"] and not self.state["paused"]:
            self.move_snake()
        self.draw_board()
        self.root.after(self.state["speed"], self.game_loop)


def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()

