from django.db import models


class Item(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title


class ItemCombo(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField('inventory.Item')

    def __unicode__(self):
        return self.title
