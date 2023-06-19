"""In the forest there is one Keeper and many creatures"""
from django.db import models # noqa: F401


class Forest(models.Model):
    title = models.CharField(max_length=20, unique=True)
    earth = models.CharField(max_length=20)

    def __str__(self):
        return f"Forest: {self.title}, {self.earth}"


class Keeper(models.Model):
    keeper_name = models.CharField(max_length=20)
    forest = models.OneToOneField(Forest, on_delete=models.CASCADE)

    def __str__(self):
        return f"Keeper: {self.keeper_name}, Forest: {self.forest}"


class Food(models.Model):
    food_title = models.CharField(max_length=20)
    energy = models.IntegerField(default=0)

    def __str__(self):
        return f"Food: {self.food_title}"


class Creature(models.Model):
    creature_name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    age = models.IntegerField()
    forest = models.ForeignKey(Forest, on_delete=models.SET_NULL, blank=True, null=True)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return f"Creature: {self.creature_name}, {self.age}, Forest: {self.forest}"
