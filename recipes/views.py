from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                #to access Recipe model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
#to protect function-based views
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart
from django.db.models import Q

# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

#define function-based view - records()
#keep protected
#@login_required
def records(request):
   #create an instance of RecipeSearchForm defined in recipes/forms.py
   form = RecipeSearchForm(request.POST or None)
   recipes_df=None   #initialize dataframe to None
   chart = None    #initialize chart to None


   #check if the button is clicked
   if request.method =='POST':
      #read book_title and chart_type
      ingredient = request.POST.get('ingredient')
      chart_type = request.POST.get('chart_type')

      #apply filter to extract data
      qs =Recipe.objects.filter(Q(ingredients__icontains=ingredient))
      if qs:      #if data found
         #convert the queryset values to pandas dataframe
         recipes_df=pd.DataFrame(qs.values(), columns=['id', 'name', 'ingredients', 'cooking_time', 'description']) 
         #call get_chart by passing chart_type from user input, sales dataframe and labels
         chart=get_chart(chart_type, recipes_df)

         links = []

         for e, nam in enumerate(recipes_df['name']):
            nam = '<a href="/list/' + str(recipes_df['id'][e]) + '">' + str(nam) + '</a>'
            links.append(nam)

         recipes_df['name'] = links

         #convert the dataframe to HTML
         recipes_df=recipes_df.to_html(index=False, escape=False, classes='table table-success table-striped')

   #pack up data to be sent to template in the context dictionary
   context={
           'form': form,
           'recipes_df': recipes_df,
           'chart': chart
            }

   #load the recipes/record.html page using the data just prepared    
   return render(request, 'recipes/records.html', context)

# Create recipe class based view
class RecipeListView(LoginRequiredMixin, ListView):           #class-based “protected” view
   model = Recipe                         #specify model
   template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):                   #class-based “protected” view
   model = Recipe                                        #specify model
   template_name = 'recipes/detail.html'                 #specify template

