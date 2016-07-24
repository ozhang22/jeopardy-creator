from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(name='Date created')

    def __str__(self):
        return self.name


class Category(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Clue(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField
    amount = models.IntegerField
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.category + " " + self.amount


class Answer(models.Model):
    clue = models.OneToOneField(Clue, on_delete=models.CASCADE)
    text = models.TextField

    def __str__(self):
        return self.clue
