from django.contrib import admin
from lassie.dialogue_tree.models import Tree, TreeMenu, TreeTopic

     
class TreeTopicInline(admin.StackedInline):
    model = TreeTopic
    
class TreeMenuInline(admin.StackedInline):
    model = TreeMenu
    fields = ('title',)
    can_delete = False
    max_num = 1;
    inlines = [TreeTopicInline,]
        

# Main content type admins:

class TreeTopicAdmin(admin.ModelAdmin):
    model = TreeTopic


class TreeMenuAdmin(admin.ModelAdmin):
    model = TreeMenu
    inlines = [TreeTopicInline,]


class TreeAdmin(admin.ModelAdmin):
    model = Tree
    inlines = [TreeMenuInline,]


admin.site.register(Tree, TreeAdmin)