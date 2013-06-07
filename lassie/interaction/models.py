from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Voice(models.Model):
    """
    Describes a voice actor reference.
    """
    title = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title
        

class Dialogue(models.Model):
    """
    Describes an individual unit of dialogue:
    Dialogue is a single statement delivered by a single actor.
    """
    index = models.PositiveIntegerField(default=0)
    puppet = models.CharField(max_length=40)
    tone = models.CharField(max_length=40, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    sound = models.CharField(max_length=40, blank=True)
    subtitle = models.TextField('Subtitle*', blank=True)
    voice = models.ForeignKey('interaction.Voice', null=True, blank=True)
    action = models.ForeignKey('interaction.Action')
    
    class Meta:
        ordering = ['index']
        verbose_name_plural = 'Dialogue'
            
    def __unicode__(self):
        return self.subtitle


class Action(models.Model):
    """
    Defines an actionable trigger.
    Actions run an environment script, and provide a collection of related dialogue.
    """
    index = models.PositiveIntegerField(default=0)
    title = models.CharField('Action title*', max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    script = models.TextField(blank=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey()
    
    class Meta:
        ordering = ['index']
        
    def __unicode__(self):
        return self.title
        

