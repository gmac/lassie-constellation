from django.contrib import admin

from lassie.scene.models import Scene, SceneObject


class SceneObjectAdmin(admin.TabularInline):
    model = SceneObject
    fields = ('uid',)


class SceneAdmin(admin.ModelAdmin):
    model = Scene
    list_display = ('title', 'uid', 'notes',)
    inlines = [SceneObjectAdmin,]


admin.site.register(Scene, SceneAdmin)