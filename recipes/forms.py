from django import forms
from django.forms import TextInput, Select, ModelForm
from django.core.exceptions import ValidationError
#import gettext_lazy() as _() for future translation of site
from django.utils.translation import gettext_lazy as _

from .models import Recipe



CHART_CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )



class RecipeSearchForm(forms.Form):
    ingredient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search by Ingredient', 'class': 'ingredient-input input-box'}),
        
        max_length=100,
        required=False,
    )
    chart_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'chart-input input-box'}),choices=CHART_CHOICES, required=True)

    #override clean() method and validate recipe name data
    def clean_recipe_name(self):
        data = self.cleaned_data.get("recipe_name")

        if not data:
            raise forms.ValidationError(_('Please enter a valid recipe name'))
        return data