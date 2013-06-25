import json
from django import template
from django.contrib.contenttypes.models import ContentType
from lassie.dialoguetree.models import Tree, TreeMenu

register = template.Library()

@register.inclusion_tag('templatetags/topic-manager.html')
def topic_manager(model):
    content_id = model.id
    enable_topics = False
    tree_menus = list()
    
    # Enable topics for Tree models:
    if (model):
        enable_topics = (ContentType.objects.get_for_model(model).model == 'tree')
        tree_menus = list(TreeMenu.objects.filter(tree=model.id).values())
        
        # Create a root menu topic, if none exists.
        if (not tree_menus):
            menu = TreeMenu(tree=model)
            menu.save()
            #tree_menus.push(menu)
    
    # Format reference ids as API URIs:
    for menu in tree_menus:
        menu['id'] = '/api/v1/treemenu/{0}/'.format(menu['id'])
    
    return {
        'content_id': content_id,
        'enable_topics': enable_topics,
        'menus_json': json.dumps(tree_menus)
    }