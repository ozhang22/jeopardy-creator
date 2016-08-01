from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
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


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('creator:user', args=(user.id,)))
            else:
                return render(request, 'creator/login.html', {
                    'error_message': "Your user is deactivated. Please contact the administrator.",
                })
        else:
            return render(request, 'creator/login.html', {
                'error_message': "You have entered invalid credentials. Please try again.",
            })
    else:
        return render(request, 'creator/login.html',)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('creator:index', args=()))
