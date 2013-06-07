from django.contrib import admin

from lassie.scene.models import Scene


class SceneAdmin(admin.ModelAdmin):
    model = Scene
    list_display = ('title', 'uid', 'notes',)


admin.site.register(Scene)