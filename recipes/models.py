from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField(default='This recipe promises not to dissappoint')
    ingredients=models.CharField(max_length=255)
    cooking_time=models.PositiveIntegerField(help_text= 'in minutes')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    

    def __str__(self): 
        return (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"

        )

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients.split(', ')) < 4:
            return 'Easy'
        elif self.cooking_time < 10 and len(self.ingredients.split(', ')) >= 4:
            return 'Medium'
        elif self.cooking_time >= 10 and len(self.ingredients.split(', ')) < 4:
            return 'Intermediate'
        elif self.cooking_time >= 10 and len(self.ingredients.split(', ')) >= 4:
            return 'Hard'

    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})

