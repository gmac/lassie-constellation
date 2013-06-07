from django.db import models


class Item(models.Model):
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField('Title*', max_length=255)
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title


class ItemCombo(models.Model):
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField('inventory.Item')

    def __unicode__(self):
        return self.title

