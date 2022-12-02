from django.shortcuts import render

from .models import Laptop

def index(request):
  laptops = Laptop.objects.order_by('-created')
  context = {'laptops': laptops}
  return render(request, 'laptop/index.html', context)


def item(request, id):
  item = Laptop.objects.get(id=id)
  context = {'item': item}
  return render(request, 'laptop/item.html', context)
