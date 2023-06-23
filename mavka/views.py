from math import sqrt

from django.http import HttpResponse
from django.shortcuts import render

from .forms import TriangleForm


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
