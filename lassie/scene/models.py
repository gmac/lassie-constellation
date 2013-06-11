from django.db import models


class Scene(models.Model):
    """
    Describes an individual scene layout within the world.
    """
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    # bgimage = models.CharField(max_length=255, blank=True)
    # music = models.CharField(max_length=255, blank=True)
    # soundfx = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title


class Layer(models.Model):
    """
    Describes an individual interactive object within a scene.
    """
    scene = models.ForeignKey('scene.Scene')
    slug = models.SlugField(default='')
    title = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True)
    index = models.SmallIntegerField(default=0)
    grid = models.SlugField(blank=True)
    opacity = models.PositiveSmallIntegerField(default=100)
    parallax_axis = models.CharField(max_length=10, blank=True)
    subtitle_color = models.CharField(max_length=10, default='#ffffff')
    visible = models.BooleanField(default=True)
    
    # Cursor settings
    cursor_enabled = models.BooleanField(default=True)
    cursor_hover = models.CharField(max_length=40, blank=True)
    
    # Floating layer order
    float_enabled = models.BooleanField(default=False)
    float_x = models.SmallIntegerField(default=0)
    float_y = models.SmallIntegerField(default=0)
    
    # Filter references
    filter_scale = models.CharField(max_length=40, blank=True)
    filter_color = models.CharField(max_length=40, blank=True)
    filter_speed = models.CharField(max_length=40, blank=True)
    
    # Hit area
    hit_h = models.PositiveSmallIntegerField(default=0)
    hit_w = models.PositiveSmallIntegerField(default=0)
    hit_x = models.SmallIntegerField(default=0)
    hit_y = models.SmallIntegerField(default=0)
    
    # Image display
    img = models.CharField(max_length=255, blank=True)
    img_h = models.PositiveSmallIntegerField(default=0)
    img_w = models.PositiveSmallIntegerField(default=0)
    img_x = models.SmallIntegerField(default=0)
    img_y = models.SmallIntegerField(default=0)
    
    # Mapping position
    map_orientation = models.SmallIntegerField(default=0)
    map_x = models.SmallIntegerField(default=0)
    map_y = models.SmallIntegerField(default=0)
    
    # Editor settings
    editor_visible = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title


class Grid(models.Model):
    scene = models.ForeignKey('scene.Scene')
    slug = models.SlugField(default='')
    notes = models.CharField(max_length=255, blank=True)
    data = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.slug


class Matrix(models.Model):
    scene = models.ForeignKey('scene.Scene')
    slug = models.SlugField(default='')
    notes = models.CharField(max_length=255, blank=True)
    type = models.SmallIntegerField(default=0)
    axis = models.SmallIntegerField(default=0)
    # Node A (origin)
    a_x = models.SmallIntegerField(default=0)
    a_y = models.SmallIntegerField(default=0)
    a_value = models.CharField(max_length=10, blank=True)
    # Node B (outlier)
    b_x = models.SmallIntegerField(default=0)
    b_y = models.SmallIntegerField(default=0)
    b_value = models.CharField(max_length=10, blank=True)
    
    def __unicode__(self):
        return self.slug

    