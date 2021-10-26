from django.urls import path
from .views import genre_list_view

app_name = 'main'
urlpatterns = [
    path('genre/', genre_list_view, name="genre_list")
]
