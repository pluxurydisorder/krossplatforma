from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Основная логика игры
class JumpingBallsGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.moves = 0
        self.board = [1, 1, 1, 1, 0, 2, 2, 2, 2]
        self.create_board()

    def create_board(self):
        self.clear_widgets()
        board_layout = BoxLayout(orientation="horizontal")
        for i, cell in enumerate(self.board):
            text = "." if cell == 0 else ("S" if cell == 1 else "G")
            button = Button(text=text, on_press=lambda btn, idx=i: self.make_move(idx))
            board_layout.add_widget(button)
        self.add_widget(board_layout)
        self.add_widget(Label(text=f"Moves: {self.moves}"))

    def make_move(self, idx):
        # Проверяем возможность хода
        empty_idx = self.board.index(0)
        if abs(idx - empty_idx) in [1, 2]:  # Прямой ход или прыжок
            self.board[empty_idx], self.board[idx] = self.board[idx], self.board[empty_idx]
            self.moves += 1
            self.create_board()
            if self.check_win():
                self.add_widget(Label(text="YOU WIN!"))

    def check_win(self):
        return self.board[:4] == [2, 2, 2, 2] and self.board[5:] == [1, 1, 1, 1]

# Основной класс приложения
class JumpingBallsApp(App):
    def build(self):
        return JumpingBallsGame()

if __name__ == "__main__":
    JumpingBallsApp().run()