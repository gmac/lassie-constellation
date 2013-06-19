from django.db import models

#from lassie.inventory.interaction import Action

class InventoryCollection(models.Model):
    '''
    Describes a collection of inventory items that may be assigned to an avatar.
    '''
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField('inventory.Item', blank=True, null=True)
    
    def __unicode__(self):
        return self.slug
        

class DefaultResponse(models.Model):
    '''
    Describes a collection of default responses that may be assigned to an avatar.
    '''
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.slug

    
class Avatar(models.Model):
    '''
    Describes a playable character.
    '''
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    inventory_collection = models.ForeignKey('player.InventoryCollection')
    default_response = models.ForeignKey('player.DefaultResponse')
    voice = models.ForeignKey('interaction.Voice')
    
    def __unicode__(self):
        return self.slug

    