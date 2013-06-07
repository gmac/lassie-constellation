from django.contrib import admin

from lassie.interaction.admin import SingleActionAdmin, MultiActionAdmin
from lassie.inventory.models import Item, ItemCombo


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('title', 'uid', 'notes',)
    inlines = [MultiActionAdmin,]


class ItemComboAdmin(admin.ModelAdmin):
    model = ItemCombo
    filter_horizontal = ('items',)
    list_display = ('title', 'uid', 'notes',)
    inlines = [SingleActionAdmin,]


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCombo, ItemComboAdmin)