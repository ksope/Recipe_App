from django.urls import path
from .views import home
from .views import RecipeListView, RecipeDetailView, records

#specify the app name
app_name = 'recipes'

#URL configuration which maps a route with it's corresponding view
urlpatterns = [
   path('', home, name='home'),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('records/', records, name='records'),
]