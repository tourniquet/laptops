from django.db import models

class Brand(models.Model):
  name = models.CharField(max_length=20, unique=True)

  class Meta:
    verbose_name_plural = 'brands'

  def __str__(self):
    return f'{self.name}'


class Model(models.Model):
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  name = models.CharField(max_length=20, unique=True)

  class Meta:
    verbose_name_plural = 'models'

  def __str__(self):
    return f'{self.name}'


class Laptop(models.Model):
  title = models.CharField(max_length=100)
  model = models.ForeignKey(Model, on_delete=models.CASCADE)
  description = models.TextField()
  status = models.BooleanField(default=True) # is it Sold or Available for sale
  price = models.IntegerField()
  quantity = models.IntegerField(default=1)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'laptops'

  def __str__(self):
    return f'{self.title}'
