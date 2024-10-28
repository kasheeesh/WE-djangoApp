from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateGameView.as_view(), name='create_game'),
    path('play/<int:game_id>/', views.GamePlayView.as_view(), name='game_play'),
    path('status/<int:game_id>/', views.GameStatusView.as_view(), name='game_status'),
]
