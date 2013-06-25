from django.contrib import admin
from lassie.dialoguetree.models import Tree, TreeMenu, TreeTopic


# Main content type admins:

class TreeTopicAdmin(admin.ModelAdmin):
    model = TreeTopic


class TreeMenuAdmin(admin.ModelAdmin):
    model = TreeMenu


class TreeAdmin(admin.ModelAdmin):
    model = Tree


admin.site.register(Tree, TreeAdmin)