from django.contrib import admin
from lassie.player.models import InventoryCollection, DefaultResponse, Avatar


class DefaultResponseAdmin(admin.ModelAdmin):
    model = DefaultResponse
    list_display = ('slug', 'title', 'notes',)
    

class InventoryCollectionAdmin(admin.ModelAdmin):
    model = InventoryCollection
    filter_horizontal = ('items',)
    list_display = ('slug', 'title', 'notes',)
    

class AvatarAdmin(admin.ModelAdmin):
    model = Avatar
    list_display = ('slug', 'title', 'notes',)


admin.site.register(InventoryCollection, InventoryCollectionAdmin)
admin.site.register(DefaultResponse, DefaultResponseAdmin)
admin.site.register(Avatar, AvatarAdmin)