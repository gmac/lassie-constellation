from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Voice(models.Model):
    """
    Describes a voice actor reference.
    """
    title = models.CharField(max_length=255)
    subtitle_color = models.CharField(max_length=10, default='#FFFFFF')
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title


# class Intonation(models.Model):
#     """
#     Describes a dialogue intonation level, used to control character expressions.
#     """
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(default='')
#     notes = models.CharField(max_length=255, blank=True)
# 
#     def __unicode__(self):
#         return self.title


class Dialogue(models.Model):
    """
    Describes an individual unit of dialogue:
    Dialogue is a single statement delivered by a single actor.
    """
    index = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default='')
    related_target = models.SlugField(default='')
    tone = models.CharField(max_length=40, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    sound = models.CharField(max_length=40, blank=True)
    subtitle = models.TextField('Subtitle*', blank=True)
    voice = models.ForeignKey('interaction.Voice')
    action = models.ForeignKey('interaction.Action')
    
    class Meta:
        ordering = ['index']
        verbose_name_plural = 'Dialogue'
            
    def __unicode__(self):
        return self.subtitle


class ActionType(models.Model):
    """
    Available game interactions. Each game action will conform to an interaction type.
    """
    title = models.CharField(max_length=255, blank=True)
    is_generic = models.BooleanField('Generic action type', default=False)
    is_item = models.BooleanField('Relates to items', default=False)
    
    def __unicode__(self):
        return self.title
        

class Action(models.Model):
    """
    Defines an actionable trigger.
    Actions run an environment script, and provide a collection of related dialogue.
    """
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    grammar = models.CharField(max_length=255, blank=True)
    script = models.TextField(blank=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey()
    related_item = models.ForeignKey('inventory.Item', blank=True, null=True)
    action_type = models.ForeignKey('interaction.ActionType')
    
    def __unicode__(self):
        return self.title

