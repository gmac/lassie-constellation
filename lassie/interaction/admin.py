from django.contrib import admin
from django.contrib.contenttypes import generic

from lassie.interaction.models import Voice, Dialogue, Action


# Global Action admin components:

class SingleActionAdmin(generic.GenericStackedInline):
    '''
    Defines an admin control for a single Action editor UI.
    '''
    model = Action
    fields = ('script',)
    can_delete = False
    max_num = 1


class MultiActionAdmin(generic.GenericStackedInline):
    '''
    Defines an admin control for multiple Action UI options.
    '''
    model = Action
    classes = 'collapse'
    fields = ('title',)
    min_num = 1
    template = "admin/multi-action.html"


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


class DialogueInlineAdmin(admin.StackedInline):
    model = Dialogue;
            

class ActionAdmin(admin.ModelAdmin):
    '''
    Configures the admin for browsing Action stores.
    Actions may only be managed through actionable components.
    Actions may NOT be added/removed through this browsing interface.
    '''
    model = Action
    exclude = ('index','object_id','content_type',)
    inlines = [DialogueInlineAdmin,]
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Voice, VoiceAdmin)
admin.site.register(Dialogue, DialogueAdmin)
admin.site.register(Action, ActionAdmin)
