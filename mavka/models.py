"""In the forest there is one Keeper and many creatures"""
from django.db import models

TITLE_CHOICES = [
    ("GET", "Get"),
    ("POST", "Post"),
    ("PUT", "Put"),
    ("HEAD", "Head"),
]


class Forest(models.Model):  # noqa: DJ10, DJ11
    title = models.CharField(max_length=20, unique=True)
    earth = models.CharField(max_length=20)

    def __str__(self):
        return f"Forest: {self.title}, {self.earth}"


class Keeper(models.Model):  # noqa: DJ10, DJ11
    keeper_name = models.CharField(max_length=20)
    power = models.CharField(max_length=20)
    forest = models.OneToOneField(Forest, on_delete=models.CASCADE)

    def __str__(self):
        return f"Keeper: {self.keeper_name}, Forest: {self.forest}"


class Food(models.Model):  # noqa: DJ10, DJ11
    food_title = models.CharField(max_length=20)
    energy = models.IntegerField(default=0)

    def __str__(self):
        return f"Food: {self.food_title}"


class Creature(models.Model):  # noqa: DJ10, DJ11
    creature_name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    age = models.IntegerField()
    forest = models.ForeignKey(Forest, on_delete=models.SET_NULL, blank=True, null=True)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return f"Creature: {self.creature_name}, {self.age}, {self.color}, {self.forest}"


class LogModel(models.Model):  # noqa: DJ10, DJ11
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=5, choices=TITLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Response: {self.path}, {self.method}, {self.created_at}, {self.data}"
