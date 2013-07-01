from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Options:

class ActionType(models.Model):
    """
    Available game interactions. Each game action will conform to an interaction type.
    """
    slug = models.SlugField()
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True)
    is_custom = models.BooleanField('Custom action type', default=False)
    is_item = models.BooleanField('Relates to items', default=False)
        
    def __unicode__(self):
        return self.label
                

class Intonation(models.Model):
    """
    Describes a dialogue intonation level, used to control character expressions.
    """
    slug = models.SlugField()
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.label


class Voice(models.Model):
    """
    Describes a voice actor reference.
    """
    slug = models.SlugField()
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True)
    subtitle_color = models.CharField(max_length=10, default='#FFFFFF')

    def __unicode__(self):
        return self.label


# Fixtures:        

class Label(models.Model):
    slug = models.SlugField(blank=True)
    label = models.CharField(max_length=255, blank=True)  #I18N
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey()
    
    class Meta:
        verbose_name = 'Localized label'
        verbose_name_plural = verbose_name
        
    def __unicode__(self):
        return self.label


class Action(models.Model):
    """
    Defines an actionable trigger.
    Actions run an environment script, and provide a collection of related dialogue.
    """
    slug = models.SlugField(blank=True)
    notes = models.CharField(max_length=255, blank=True)
    script = models.TextField(blank=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey()
    related_item = models.ForeignKey('core.Item', blank=True, null=True)
    action_type = models.ForeignKey('core.ActionType')
    label = generic.GenericRelation('core.Label')
    
    def __unicode__(self):
        return '{0}'.format(self.action_type.id)


class Avatar(models.Model):
    """
    Describes a playable character.
    """
    slug = models.SlugField(unique=True)
    notes = models.CharField(max_length=255, blank=True)
    label = generic.GenericRelation('core.Label')
    inventory_collection = models.ForeignKey('core.Inventory')
    default_behavior = models.ForeignKey('core.DefaultActionSet')
    voice = models.ForeignKey('core.Voice')

    def __unicode__(self):
        return self.slug


class DefaultActionSet(models.Model):
    """
    Describes a collection of default actions that may be assigned to an avatar.
    """
    slug = models.SlugField(unique=True)
    notes = models.CharField(max_length=255, blank=True)
    actions = generic.GenericRelation(Action)
    
    def __unicode__(self):
        return self.slug
                

class Dialogue(models.Model):
    """
    Describes an individual unit of dialogue:
    Dialogue is a single statement delivered by a single actor.
    """
    slug = models.SlugField(blank=True)
    notes = models.CharField(max_length=255, blank=True)
    index = models.PositiveIntegerField(default=0)
    tone = models.SlugField(default='', blank=True)
    sound = models.CharField(max_length=40, blank=True)
    title = models.TextField(blank=True) #I18N
    related_target = models.SlugField(blank=True)
    voice = models.ForeignKey('core.Voice')
    action = models.ForeignKey('core.Action')
    
    class Meta:
        ordering = ['index']
        verbose_name_plural = 'Dialogue'

    def __unicode__(self):
        return self.title


class Inventory(models.Model):
    """
    Describes a collection of inventory items that may be assigned to an avatar.
    """
    slug = models.SlugField(unique=True)
    notes = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField('core.Item', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Inventories'
        
    def __unicode__(self):
        return self.slug
                

class Item(models.Model):
    slug = models.SlugField(unique=True)
    notes = models.CharField(max_length=255, blank=True)
    label = generic.GenericRelation('core.Label')
    actions = generic.GenericRelation('core.Action')
    
    def __unicode__(self):
        return self.slug


class ItemCombo(models.Model):
    slug = models.SlugField(unique=True)
    notes = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField('core.Item')
    actions = generic.GenericRelation('core.Action')
    
    def __unicode__(self):
        return self.slug

