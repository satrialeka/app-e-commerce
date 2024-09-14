from django.forms import ModelForm
from main.models import Sneakers

class SneakersForm(ModelForm):
    class Meta:
        model = Sneakers
        fields = ["name", "price", "description", "image", "quantity"]