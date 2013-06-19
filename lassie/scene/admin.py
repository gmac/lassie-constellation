from django.contrib import admin
from lassie.scene.models import Scene, Layer


class LayerInlineAdmin(admin.TabularInline):
    model = Layer
    fields = ('slug', 'title', 'image',)
    extra = 2


class SceneAdmin(admin.ModelAdmin):
    model = Scene
    list_display = ('slug', 'title', 'notes',)
    inlines = [LayerInlineAdmin,]


admin.site.register(Scene, SceneAdmin)