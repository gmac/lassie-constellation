from django.db import models


class TreeTopic(models.Model):
    """
    Describes an individual topic line within a dialogue tree:
    A Topic contains an action (script and dialogue), and tree navigation prompts.
    """
    slug = models.SlugField()
    index = models.IntegerField(default=0)
    title = models.CharField(max_length=255, blank=True)
    menu = models.ForeignKey('dialogue_tree.TreeMenu')
    
    def __unicode__(self):
        return self.title
                

class TreeMenu(models.Model):
    """
    Describes a collection of Topics composing a single menu within a dialogue tree.
    """
    slug = models.SlugField()
    title = models.CharField(max_length=255, blank=True)
    topic = models.ForeignKey('dialogue_tree.TreeTopic', null=True, blank=True)
    tree = models.ForeignKey('dialogue_tree.Tree', null=True, blank=True)
    
    def __unicode__(self):
        return self.title


class Tree(models.Model):
    """
    Describes a complete tree of dialogue, composed of multiple menus, each with sub-topics.
    """
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = 'Dialogue Tree'
    
    def __unicode__(self):
        return self.title
