from django.forms import ModelForm
from .models import Photo
from django import forms
class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }