from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'laptop'
urlpatterns = [
  # Home page
  path('', views.index, name='index'),
  path('<slug:slug>-<int:id>/', views.item, name='item'), # use slug urls, like /dell-inspiron-5110-44 or /hp-pavilion-dv6-19
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
