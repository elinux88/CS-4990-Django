from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator

class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    category = models.ForeignKey('Category')
    sku = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:updateitem', kwargs={'pk': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True);

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
