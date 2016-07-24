from django.views import generic

from .models import User, Game, Category, Clue, Answer


class IndexView(generic.ListView):
    template_name = 'creator/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all


class UserView(generic.DetailView):
    model = User
    template_name = 'creator/user.html'


class GameView(generic.DetailView):
    model = Game
    template_name = 'creator/game.html'
