from django.contrib import admin
from .models import Action, ActionType, Avatar, DefaultActionSet, Dialogue, Intonation, Inventory, Item, ItemCombo, Voice


# Package-specific admin/browsing tools:

class ActionAdmin(admin.ModelAdmin):
    """
    Configures the admin for browsing Action stores.
    Actions may only be managed through actionable components.
    Actions may NOT be added/removed through this browsing interface.
    """
    list_display = ('action_type','content_type','object_id','related_item',)
    exclude = ('object_id','content_type',)
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ActionTypeAdmin(admin.ModelAdmin):
    """
    Configures the admin for listing out action types.
    """
    list_display = ('label', 'is_item', 'is_custom',)


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('slug', 'notes',)


class DialogueAdmin(admin.ModelAdmin):
    """
    Configures the admin for browsing Dialogue stores.
    Dialogue may only be managed through an Action admin.
    Dialogue may NOT be added/removed through this browsing interface.
    """
    list_display = ('title', 'voice', 'id',)
    exclude = ('action',)
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class DefaultActionSetAdmin(admin.ModelAdmin):
    list_display = ('slug', 'notes',)
            

class IntonationAdmin(admin.ModelAdmin):
    list_display = ('label', 'notes',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('slug', 'notes',)


class ItemComboAdmin(admin.ModelAdmin):
    list_display = ('slug', 'notes',)
    filter_horizontal = ('items',)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'notes',)
    filter_horizontal = ('items',)


class VoiceAdmin(admin.ModelAdmin):
    """
    Configures the admin for listing out Voice options.
    """
    list_display = ('label', 'notes',)


admin.site.register(Action, ActionAdmin)
admin.site.register(ActionType, ActionTypeAdmin)
admin.site.register(Avatar, AvatarAdmin)
admin.site.register(DefaultActionSet, DefaultActionSetAdmin)
admin.site.register(Dialogue, DialogueAdmin)
admin.site.register(Intonation, IntonationAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCombo, ItemComboAdmin)
admin.site.register(Voice, VoiceAdmin)
