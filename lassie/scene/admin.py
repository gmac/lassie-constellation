from django.contrib import admin
from lassie.scene.models import Scene, Layer


class LayerAdmin(admin.TabularInline):
    model = Layer
    fields = ('slug',)


class SceneAdmin(admin.ModelAdmin):
    model = Scene
    list_display = ('slug', 'title', 'notes',)
    inlines = [LayerAdmin,]


admin.site.register(Scene, SceneAdmin)