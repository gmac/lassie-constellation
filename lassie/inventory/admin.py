from django.contrib import admin
from lassie.interaction.admin import ActionInline
from lassie.inventory.models import Item, ItemCombo


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('slug', 'title', 'notes',)
    list_display = ('title', 'slug', 'notes',)
    #inlines = [ActionInline,]


class ItemComboAdmin(admin.ModelAdmin):
    model = ItemCombo
    filter_horizontal = ('items',)
    list_display = ('title', 'slug', 'notes',)
    #inlines = [ActionInline,]


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCombo, ItemComboAdmin)