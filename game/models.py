from django.db import models


class GameModel(models.Model):
    SPACE = ' '
    PLAYER_WIN = "PL"
    ONGOING = "OG"
    player_name = models.CharField(max_length=50)
    board = models.CharField(max_length=30)

    def two_d_board(self):
        return [list(self.board[:5]), list(self.board[5:10]), list(self.board[10:15]), self.board[15:20], self.board[20:25], self.board[25:]]

    @staticmethod
    def flatten(grid):
        return ''.join([''.join(row) for row in grid])

    def __str__(self):
        grid = self.two_d_board()
        grid = ["|".join(cell) for cell in grid]
        return "\n".join(grid)

    def write_word(self, row, list):
        grid = self.two_d_board()
        for i in range(5):
            grid[row][i] = list[i]
            self.board = GameModel.flatten(grid)

# Create your models here.
