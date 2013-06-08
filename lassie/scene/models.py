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
	depth = models.SmallIntergerField(default=0)
	grid = models.CharField(max_length=40, blank=True)
	opacity = models.PositiveSmallIntergerField(default=100)
	parallax_axis = models.CharField(max_length=10, blank=True)
	subtitle_color = models.CharField(max_length=10, default='#ffffff')
	visible = models.BooleanField(default=True)
	
	# Cursor settings
	cursor_enabled = models.BooleanField(default=True)
	cursor_hover = models.CharField(max_length=40, blank=True)
	
	# Floating layer order
	float_enabled = models.BooleanField(default=False)
	float_x = models.SmallIntergerField(default=0)
	float_y = models.SmallIntergerField(default=0)
	
	# Filter references
	filter_scale = models.CharField(max_length=40, blank=True)
	filter_color = models.CharField(max_length=40, blank=True)
	filter_speed = models.CharField(max_length=40, blank=True)
	
	# Hit area
	hit_h = models.PositiveSmallIntergerField(default=0)
	hit_w = models.PositiveSmallIntergerField(default=0)
	hit_x = models.SmallIntergerField(default=0)
	hit_y = models.SmallIntergerField(default=0)
	
	# Image display
	img = models.CharField(max_length=255, blank=True)
	img_h = models.PositiveSmallIntergerField(default=0)
	img_w = models.PositiveSmallIntergerField(default=0)
	img_x = models.SmallIntergerField(default=0)
	img_y = models.SmallIntergerField(default=0)
	
	# Mapping position
	map_orientation = models.SmallIntergerField(default=0)
	map_x = models.SmallIntergerField(default=0)
	map_y = models.SmallIntergerField(default=0)
	
	# Editor settings
	editor_visible = models.BooleanField(default=True)
	
    def __unicode__(self):
        return self.title
