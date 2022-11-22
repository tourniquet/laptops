from django.urls import path

from . import views

app_name = 'laptop'
urlpatterns = [
  # Home page
  path('', views.index, name='index'),
  path('item/<int:id>/', views.item, name='item'),
]
