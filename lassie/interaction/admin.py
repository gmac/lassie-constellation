from django.contrib import admin
from django.contrib.contenttypes import generic
from lassie.interaction.models import Voice, Dialogue, ActionType, Action


# Global Action admin components:

class ActionInline(generic.GenericInlineModelAdmin):
    '''
    Defines an admin control for a single Action editor UI.
    '''
    model = Action
    template = "admin/edit_inline/actions-inline.html"


# Package-specific admin/browsing tools:

class VoiceAdmin(admin.ModelAdmin):
    '''
    Configures the admin for listing out Voice options.
    '''
    list_display = ('title','notes',)
    
    
class DialogueAdmin(admin.ModelAdmin):
    '''
    Configures the admin for browsing Dialogue stores.
    Dialogue may only be managed through an Action admin.
    Dialogue may NOT be added/removed through this browsing interface.
    '''
    model = Dialogue
    exclude = ('action',)
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
  

class ActionAdmin(admin.ModelAdmin):
    '''
    Configures the admin for browsing Action stores.
    Actions may only be managed through actionable components.
    Actions may NOT be added/removed through this browsing interface.
    '''
    model = Action
    exclude = ('object_id','content_type',)
    list_display = ('action_type','content_type','object_id','related_item',)
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Voice, VoiceAdmin)
admin.site.register(Dialogue, DialogueAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(ActionType)
