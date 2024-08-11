
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('search_venues/', views.search_venues, name = "search_venues"),
    
]
