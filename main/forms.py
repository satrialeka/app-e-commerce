from django.forms import ModelForm
from main.models import Sneakers
from django.utils.html import strip_tags

class SneakersForm(ModelForm):
    class Meta:
        model = Sneakers
        fields = ["name", "price", "description", "image", "quantity"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        return strip_tags(quantity)