from math import sqrt

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .forms import CreatureModelForm, TriangleForm
from .models import Creature


def index(request):
    return HttpResponse("<h3>Hello!</h3>")


def triangle(request):
    gip = None
    if request.method == "POST":
        form_data = TriangleForm(request.POST)
        if form_data.is_valid():
            a = form_data.cleaned_data["size_a"]
            b = form_data.cleaned_data["size_b"]
            gip = round(sqrt((int(a) ** 2) + (int(b) ** 2)), 2)
            return render(request, "mavka/triangle.html", {"gip": gip, "form": form_data})
    else:
        form_data = TriangleForm()
    return render(request, "mavka/triangle.html", {"form": form_data})


class CreaturesList(ListView):
    model = Creature
    template_name = "mavka/creatures_list.html"
    context_object_name = "creatures"


def create_creature(request):
    if request.method == "POST":
        form = CreatureModelForm(request.POST)
        if form.is_valid():
            creature = Creature.objects.create(
                creature_name=form.cleaned_data["creature_name"],
                color=form.cleaned_data["color"],
                age=form.cleaned_data["age"],
                forest=form.cleaned_data["forest"],
            )
            return redirect(reverse("creature_detail", args=(creature.id,)))
    else:
        form = CreatureModelForm()
    return render(request, "mavka/create_creature.html", {"form": form})


class CreatureDetail(DetailView):
    model = Creature


def update_creature(request, pk):
    creature = get_object_or_404(Creature, pk=pk)
    if request.method == "POST":
        form = CreatureModelForm(request.POST, instance=creature)
        if form.is_valid():
            creature.creature_name = form.cleaned_data["creature_name"]
            creature.color = form.cleaned_data["color"]
            creature.age = form.cleaned_data["age"]
            creature.forest = form.cleaned_data["forest"]
            creature.save()
            return redirect(reverse("creature_detail", args=(creature.id,)))
    else:
        form = CreatureModelForm(instance=creature)
    return render(request, "mavka/update_creature.html", {"form": form, "creature": creature})
