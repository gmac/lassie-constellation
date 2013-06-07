from django.db import models

class Scene(models.Model):
    """
    Describes an individual scene layout within the world.
    """
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title


class SceneObject(models.Model):
    """
    Describes an individual interactive object within a scene.
    """
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.title

   
class SceneObjectState(models.Model):
    """
    Describes an individual scene object state.
    """
    uid = models.CharField('Reference id', max_length=40, unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.title