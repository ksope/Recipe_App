from django.test import TestCase

from .models import Recipe
from .forms import RecipeSearchForm

# Create your tests here.
class RecipeModelTest(TestCase):
   def setUpTestData():
      # Set up non-modified objects used by all test methods
      Recipe.objects.create(name='Jack Potatoes', ingredients='potatoes, oil, bacon, vegetables, butter', cooking_time='25')

   #test to see if the book’s name is initialized as expected
   def test_recipe_name(self):
      # Get a book object to test
      recipe = Recipe.objects.get(id=1)

      # Get the metadata for the 'name' field and use it to query its data
      field_label = recipe._meta.get_field('name').verbose_name

      # Compare the value to the expected result
      self.assertEqual(field_label, 'name')

   #test to ensure that the length of the ingredients field is a maximum of 120
   def test_ingredients_max_length(self):
         # Get a book object to test
         recipe = Recipe.objects.get(id=1)

         # Get the metadata for the 'author_name' field and use it to query its max_length
         max_length = recipe._meta.get_field('ingredients').max_length

         # Compare the value to the expected result i.e. 120
         self.assertEqual(max_length, 255)

   def test_cooking_time(self):
      recipe = Recipe.objects.get(id=1)
      recipe_cooking_time = recipe.cooking_time
      self.assertEqual(recipe_cooking_time, 25)

   def test_ingredients_list(self):
      recipe = Recipe.objects.get(id=1)
      recipe_ingredients = recipe.ingredients
      self.assertEqual(recipe_ingredients, 'potatoes, oil, bacon, vegetables, butter')

   #test to validate all fields
   def recipe_is_valid(self):
      recipe = Recipe.objects.get(id=1)
      self.assertTrue(recipe.is_valid())

    # test recipes_home_view
   def test_recipes_home_view(self):
      response = self.client.get("")
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, "recipes/recipes_home.html")

   def test_get_absolute_url(self):
      recipe = Recipe.objects.get(id=1)
      self.assertEqual(recipe.get_absolute_url(), "/list/1")

   # test RecipesListView
   def test_recipes_list_view(self):
      response = self.client.get("/list/")
      self.assertEqual(response.status_code, 302)
      #self.assertTemplateUsed(response, "recipes/main.html")

   # test RecipesDetailView
   def test_recipes_detail_view(self):
      recipe = Recipe.objects.get(id=1)
      response = self.client.get("/list/1")
      self.assertEqual(response.status_code, 302)
      #self.assertTemplateUsed(response, "recipes/detail.html")

   #test the calculate difficulty function
   def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), 'Hard')


class RecipeSearchFormTest(TestCase):
   def setUpTestData():
      # Set up non-modified objects used by all test methods
      Recipe.objects.create(name='Jack Potatoes', ingredients='potatoes, oil, bacon, vegetables, butter', cooking_time='25')

   #test the search form fields
   def test_form_fields(self):
      recipe = Recipe.objects.get(id=1)
      recipe_ingredients = recipe.ingredients
      form_data = {   
            "ingredient": recipe_ingredients,
            "chart_type": "#1",
        }
      form = RecipeSearchForm(data=form_data)
      self.assertTrue(form.is_valid())

   #search form invalid without chart type data
   def test_form_missing_data(self):
      form_data = {} 
      form = RecipeSearchForm(data=form_data)
      self.assertFalse(form.is_valid())

   # empty ingredient field, form is valid
   def test_empty_ingredient_form(self):
      recipe = Recipe.objects.get(id=1)
      recipe_ingredients = recipe.ingredients
      form_data = {   
            "ingredient": '',
            "chart_type": "#1",
        }
      form = RecipeSearchForm(data=form_data)
      self.assertTrue(form.is_valid())

   # partial ingredient field, form is valid
   def test_empty_ingredient_form(self):
      recipe = Recipe.objects.get(id=1)
      recipe_ingredients = recipe.ingredients
      form_data = {   
            "ingredient": 'pota',
            "chart_type": "#1",
        }
      form = RecipeSearchForm(data=form_data)
      self.assertTrue(form.is_valid())

   