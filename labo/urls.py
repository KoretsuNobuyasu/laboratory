from django.urls import path
from . import views

app_name = 'labo'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
]