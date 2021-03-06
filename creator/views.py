from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import generic

from creator.forms import UserForm
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


def register_user(request):
    context = RequestContext(request)

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
            )
            login(request, user)

            return HttpResponseRedirect(reverse('creator:user', args=(user.id,)))
        else:
            return render_to_response('creator/register.html', {
                    'user_form': user_form,
                    'error_message': 'You have entered invalid fields. Please try again.',
                }, context)
    else:
        user_form = UserForm()

        return render_to_response('creator/register.html', {
                'user_form': user_form,
            }, context)


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


def get_clue(request):
    context = RequestContext(request)
    row_index = None
    column_index = None
    game = None
    if request.method == 'GET':
        row_index = request.GET['row_index']
        column_index = request.GET['column_index']
        game = Game.objects.get(pk=request.GET['game_id'])

    if row_index and column_index and Game:
        category = game.category_set.all()[int(column_index)]
        if int(row_index) == 1:
            clue = category.clue_set.first()
        else:
            clue = category.clue_set.all()[int(row_index) - 1]
        return HttpResponse(clue.clue_text)

    return HttpResponse("")
