from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Начальная доска игры
board = [1, 1, 1, 1, 0, 2, 2, 2, 2]
moves = 0

def print_board():
    """Возвращает текстовую строку состояния доски."""
    return " ".join(["." if x == 0 else "S" if x == 1 else "G" for x in board])

def is_win():
    """Проверяет, достигнуто ли победное состояние."""
    return board[:4] == [2, 2, 2, 2] and board[5:] == [1, 1, 1, 1]

@app.route("/")
def index():
    """Главная страница с игрой."""
    return render_template("index.html", board=print_board(), moves=moves)

@app.route("/move", methods=["POST"])
def move():
    """Обрабатывает ход пользователя."""
    global board, moves

    data = request.get_json()
    move_from = int(data.get("from")) - 1
    move_to = int(data.get("to")) - 1

    if 0 <= move_from < 9 and 0 <= move_to < 9:
        # Проверка легальности хода
        if abs(move_from - move_to) == 1 or abs(move_from - move_to) == 2:
            if board[move_from] != 0 and board[move_to] == 0:
                board[move_to] = board[move_from]
                board[move_from] = 0
                moves += 1

                if is_win():
                    return jsonify({"status": "win", "board": print_board(), "moves": moves})

                return jsonify({"status": "ok", "board": print_board(), "moves": moves})

    return jsonify({"status": "error", "message": "Illegal move"})

@app.route("/reset", methods=["POST"])
def reset():
    """Сбрасывает игру."""
    global board, moves
    board = [1, 1, 1, 1, 0, 2, 2, 2, 2]
    moves = 0
    return jsonify({"status": "ok", "board": print_board(), "moves": moves})

if __name__ == "__main__":
    app.run(debug=True)