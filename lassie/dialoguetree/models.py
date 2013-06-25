from django.db import models

class TreeTopic(models.Model):
    """
    Describes an individual topic line within a dialogue tree:
    A Topic contains an action (script and dialogue), and tree navigation prompts.
    """
    index = models.IntegerField(default=0)
    slug = models.SlugField(default='', blank=True)
    title = models.CharField(max_length=255, blank=True) #I18N
    treemenu = models.ForeignKey('dialoguetree.TreeMenu')
    
    def __unicode__(self):
        return self.slug


class TreeMenu(models.Model):
    """
    Describes a collection of Topics composing a single menu within a dialogue tree.
    """
    slug = models.SlugField(default='', blank=True)
    path = models.CharField(max_length=255, blank=True)
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
