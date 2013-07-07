from django.contrib.contenttypes import generic
from django.db import models
from django.db.models.signals import post_save
from lassie.core.models import Action, ActionType

class TreeTopic(models.Model):
    """
    Describes an individual topic line within a dialogue tree:
    A Topic contains an action (script and dialogue), and tree navigation prompts.
    """
    index = models.IntegerField(default=0)
    slug = models.SlugField(default='', blank=True)
    directive = models.SlugField(default='', blank=True)
    label = models.ForeignKey('core.Label', blank=True, null=True)
    menu = models.ForeignKey('dialoguetree.TreeMenu')
    tree = models.ForeignKey('dialoguetree.Tree')
    action = generic.GenericRelation(Action)
    
    @staticmethod
    def save_treetopic(sender, instance, created, **kwargs):
        if (created):
            instance.action.create(action_type=ActionType.get_default())
    
    def __unicode__(self):
        return self.slug


# Create a new action in response to creating a new tree topic:
post_save.connect(TreeTopic.save_treetopic, sender=TreeTopic, dispatch_uid="save_treetopic")


class TreeMenu(models.Model):
    """
    Describes a collection of Topics composing a single menu within a dialogue tree.
    """
    slug = models.SlugField(default='', blank=True)
    topic = models.ForeignKey('dialoguetree.TreeTopic', blank=True, null=True)
    tree = models.ForeignKey('dialoguetree.Tree')
    
    def __unicode__(self):
        return self.slug


class Tree(models.Model):
    """
    Describes a complete tree of dialogue, composed of multiple menus, each with sub-topics.
    """
    slug = models.SlugField(unique=True)
    notes = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = 'Dialogue Tree'
    
    def __unicode__(self):
        return self.slug
