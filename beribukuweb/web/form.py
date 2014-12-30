from django import forms
from django.forms import ModelForm
from web.models import *

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = __"all"__

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = __"all"__

class ItemForm(ModelForm):
    jumlah = forms.IntegerField(default=0)
    class Meta:
        model = Item
        fields = __"all"__+['jumlah']

class Donatur(ModelForm):
    class Meta:
        model = Donatur
        fields = __"all"__