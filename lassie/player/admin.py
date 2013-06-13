from django.contrib import admin
from lassie.interaction.admin import ActionInline
from lassie.player.models import InventoryCollection, DefaultResponse, Avatar


class DefaultResponseAdmin(admin.ModelAdmin):
    model = DefaultResponse
    list_display = ('title', 'uid', 'notes',)
    

class InventoryCollectionAdmin(admin.ModelAdmin):
    model = InventoryCollection
    filter_horizontal = ('items',)
    list_display = ('title', 'uid', 'notes',)
    

class AvatarAdmin(admin.ModelAdmin):
    model = Avatar
    list_display = ('title', 'uid', 'notes',)


admin.site.register(InventoryCollection, InventoryCollectionAdmin)
admin.site.register(DefaultResponse, DefaultResponseAdmin)
admin.site.register(Avatar, AvatarAdmin)