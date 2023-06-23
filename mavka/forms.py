from django import forms
from django.core.exceptions import ValidationError


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
