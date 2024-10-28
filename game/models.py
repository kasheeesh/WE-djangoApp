from django.db import models


class GameModel(models.Model):
    SPACE = ' '
    PLAYER_WIN = "PW"
    PLAYER_LOST = "PL"
    ONGOING = "OG"

    player_name = models.CharField(max_length=50)
    board = models.CharField(max_length=30)
    target_word = models.CharField(max_length=5)
    current_row = models.IntegerField(default=0)

    def two_d_board(self):
        return [list(self.board[i * 5:(i + 1) * 5]) for i in range(6)]

    @staticmethod
    def flatten(grid):
        return ''.join([''.join(row) for row in grid])

    def __str__(self):
        grid = self.two_d_board()
        grid = ["|".join(cell) for cell in grid]
        return "\n".join(grid)

    def write_word(self, row, word_list):
        if row < 0 or row > 5:
            raise ValueError("Invalid row number")
        if len(word_list) != 5:
            raise ValueError("Word must be 5 letters long")

        grid = self.two_d_board()
        for i in range(5):
            grid[row][i] = word_list[i]
        self.board = GameModel.flatten(grid)
        self.current_row += 1
        self.save()

        self.check_word(''.join(word_list))

    def status(self):
        grid = self.two_d_board()
        for row in range(6):
            current_guess = ''.join(grid[row])
            if current_guess == self.target_word:
                return GameModel.PLAYER_WIN

        if self.current_row >= 6:
            return GameModel.PLAYER_LOST

        return GameModel.ONGOING

    def check_word(self, guess):
        feedback = []
        for i in range(5):
            if guess[i] == self.target_word[i]:
                feedback.append('G')
            elif guess[i] in self.target_word:
                feedback.append('Y')
            else:
                feedback.append('B')

        return feedback
