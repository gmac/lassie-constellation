from django.contrib import admin
from lassie.core.admin import LabelInline
from lassie.scene.models import Scene, Layer


class LayerInlineAdmin(admin.TabularInline):
    model = Layer
    fields = ('slug', 'group', 'image',)
    extra = 2


class SceneAdmin(admin.ModelAdmin):
    list_display = ('slug', 'notes',)
    inlines = [LabelInline, LayerInlineAdmin,]


admin.site.register(Scene, SceneAdmin)