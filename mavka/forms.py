from django import forms
from django.core.exceptions import ValidationError

from .models import Creature


class TriangleForm(forms.Form):
    size_a = forms.IntegerField(label="Size A", max_value=100, required=True)
    size_b = forms.IntegerField(label="Size B", max_value=100, required=True)

    def clean_size_a(self):
        size_a = self.cleaned_data["size_a"]
        if int(size_a) <= 0:
            raise ValidationError("OMG! Invalid size A!")
        else:
            return size_a

    def clean_size_b(self):
        size_b = self.cleaned_data["size_b"]
        if int(size_b) <= 0:
            raise ValidationError("OMG! Invalid size B!")
        else:
            return size_b


class CreatureModelForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = ["creature_name", "color", "age", "forest"]

    def clean_creature_name(self):
        creature_name = self.cleaned_data["creature_name"]
        if len(creature_name) < 2:
            raise ValidationError("There is no Creature with a name shorter than 2 characters!")
        else:
            return creature_name

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 1:
            raise ValidationError("This Creature has not yet been born!")
        else:
            return age
