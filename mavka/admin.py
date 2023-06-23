from django.contrib import admin
from .models import Creature, Food, Forest, Keeper


@admin.register(Forest)
class ForestAdmin(admin.ModelAdmin):
    list_display = ("title", "earth")


@admin.register(Keeper)
class KeeperAdmin(admin.ModelAdmin):
    list_display = ("keeper_name", "forest")


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("food_title", "energy")


@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display = ("creature_name", "color", "age", "forest")
