from django.contrib import admin

from .models import Game, Category, Clue, Answer

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Clue)
admin.site.register(Answer)
