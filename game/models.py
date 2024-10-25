from django.db import models


class GameModel(models.Model):
    SPACE = ' '
    player_name = models.CharField(max_length=50)
    board = models.CharField(max_length=30)

    def two_d_board(self):
        return [self.board[:5], self.board[5:10], self.board[10:15], self.board[15:20], self.board[20:25], self.board[25:]]

    def __str__(self):
        grid = self.two_d_board()
        grid = ["|".join(cell) for cell in grid]
        return "\n".join(grid)

# Create your models here.
