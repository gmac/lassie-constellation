from django.db import models

#from lassie.inventory.interaction import Action

class InventoryCollection(models.Model):
    '''
    Describes a collection of inventory items that may be assigned to an avatar.
    '''
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField('inventory.Item', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
        

class DefaultResponse(models.Model):
    '''
    Describes a collection of default responses that may be assigned to an avatar.
    '''
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title

    
class Avatar(models.Model):
    '''
    Describes a playable character.
    '''
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField('Title*', max_length=255)
    notes = models.CharField(max_length=255, blank=True)
    inventory_collection = models.ForeignKey('player.InventoryCollection')
    default_response = models.ForeignKey('player.DefaultResponse')
    
    def __unicode__(self):
        return self.title

    