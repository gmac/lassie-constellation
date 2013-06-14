from django.contrib import admin
from lassie.inventory.models import Item, ItemCombo


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('slug', 'title', 'notes',)


class ItemComboAdmin(admin.ModelAdmin):
    model = ItemCombo
    filter_horizontal = ('items',)
    list_display = ('slug', 'title', 'notes',)


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCombo, ItemComboAdmin)