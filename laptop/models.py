from django.db import models
from django.utils.text import slugify

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
  link = models.CharField(max_length=200) # this one may be temporary for using links to Marketplace
  slug = models.SlugField(default='', null=False) # urls like 'hp-pavilion-dv-6-45', where 45 is listing id

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)

  class Meta:
    verbose_name_plural = 'laptops'

  def __str__(self):
    return f'{self.title}'
