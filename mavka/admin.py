from django.contrib import admin
from .models import Creature, Food, Forest, Keeper, LogModel


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
    list_display = ("creature_name", "color", "age", "forest", "age_status")

    @admin.display(ordering="age", description="Status")
    def age_status(self, creature: Creature):
        if creature.age < 130:
            return "So young creature"
        elif creature.age < 190:
            return "Middle creature"
        else:
            return "Serious creature"


@admin.register(LogModel)
class LogModelAdmin(admin.ModelAdmin):
    list_display = ("path", "method", "created_at", "data")
    fieldsets = [
        ("General information", {"fields": ["path", "method"]}),
        ("Data information", {"fields": ["data"]}),
    ]
    date_hierarchy = "created_at"
    # list_editable = ("method", "created_at")
    ordering = ("created_at", "path")
    list_per_page = 10
    search_fields = ["method"]
