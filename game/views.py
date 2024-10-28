from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from .models import GameModel


class CreateGameView(View):
    def get(self, request):
        return render(request, 'game/create_game.html')

    def post(self, request):
        player_name = request.POST.get('player_name')
        target_word = request.POST.get('target_word').upper()

        game = GameModel.objects.create(
            player_name=player_name,
            board=" " * 30,
            target_word=target_word
        )

        return redirect('game_play', game_id=game.id)


class GamePlayView(View):
    def get(self, request, game_id):
        game = get_object_or_404(GameModel, id=game_id)
        context = {
            'game': game,
            'board': game.two_d_board(),
            'status': game.status()
        }
        return render(request, 'game/play_game.html', context)

    def post(self, request, game_id):
        game = get_object_or_404(GameModel, id=game_id)

        guessed_word = request.POST.get('guess').upper()

        if len(guessed_word) != 5:
            return JsonResponse({"error": "Guess must be 5 letters long"}, status=400)
        try:
            game.write_word(game.current_row, list(guessed_word))
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        feedback = game.check_word(guessed_word)

        game_status = game.status()

        return JsonResponse({
            "feedback": feedback,
            "status": game_status,
            "board": game.two_d_board()
        })


class GameStatusView(View):
    def get(self, request, game_id):
        game = get_object_or_404(GameModel, id=game_id)
        status = game.status()

        return JsonResponse({
            "status": status,
            "board": game.two_d_board(),
            "current_row": game.current_row,
            "player_name": game.player_name
        })
