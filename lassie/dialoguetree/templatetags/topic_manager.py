import json
from django import template
from django.contrib.contenttypes.models import ContentType
from lassie.dialoguetree.models import Tree, TreeMenu

register = template.Library()

@register.inclusion_tag('templatetags/topic-manager.html')
def topic_manager(model):
    
    context = {
        'content_id': 0,
        'enable_manager': False,
        'menus_json': '[]',
    }
    
    # Enable topics for Tree models:
    if (model):
        context['enable_manager'] = (ContentType.objects.get_for_model(model).model == 'tree')
    
    if (not context['enable_manager']):
        return;
    
    context['content_id'] = model.id
    tree_menus = TreeMenu.objects.filter(tree=model.id, path='0')
    
    # Create a root menu topic, if none exists.
    if (not tree_menus.count()):
        tree_menus.create(tree=model, path='0')
    
    tree_menus = list(tree_menus)
    
    # Format reference ids as API URIs:
    for menu in tree_menus:
        menu['id'] = '/api/v1/treemenu/{0}/'.format(menu['id'])
    
    context['menus_json'] = json.dumps(tree_menus)
    
    return context
