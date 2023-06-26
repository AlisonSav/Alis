from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("triangle/", views.triangle, name="triangle"),
    path("creatures_list/", views.CreaturesList.as_view(), name="creatures_list"),
    path("create_creature/", views.create_creature, name="create_creature"),
    path("update_creature/<int:pk>", views.update_creature, name="update_creature"),
    path("creature/<int:pk>", views.CreatureDetail.as_view(), name="creature_detail"),
]
