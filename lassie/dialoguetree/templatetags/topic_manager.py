import json
from django import template
from django.contrib.contenttypes.models import ContentType
from lassie.dialoguetree.models import Tree, TreeMenu, TreeTopic

register = template.Library()

@register.inclusion_tag('templatetags/tree-manager.html')
def topic_manager(model):
    
    context = {
        'enable_topics': False,
        'tree_id': 0,
        'menus_json': '[]',
        'topics_json': '[]',
    }
    
    # Enable topics for Tree models:
    if (model):
        context['enable_topics'] = (ContentType.objects.get_for_model(model).model == 'tree')
    
    if (not context['enable_topics']):
        return;
    
    context['tree_id'] = model.id
    tree_menus = TreeMenu.objects.filter(tree=model)
    
    # Create a root menu topic, if none exists.
    if (not tree_menus.count()):
        tree_menus.create(tree=model)
    
    tree_menus = list(tree_menus.values())
    tree_topics = list(TreeTopic.objects.filter(tree=model).values())
    
    for menu in tree_menus:
        menu['tree'] = '/api/v1/tree/{0}/'.format(menu['tree_id'])
        menu['topic'] = None
        if menu['topic_id']:
            menu['topic'] = '/api/v1/treetopic/{0}/'.format(menu['topic_id'])
    
    for topic in tree_topics:
        topic['tree'] = '/api/v1/tree/{0}/'.format(topic['tree_id'])
        topic['menu'] = '/api/v1/treemenu/{0}/'.format(topic['menu_id'])
        topic['label'] = None
        if topic['label_id']:
            topic['label'] = '/api/v1/label/{0}/'.format(topic['label_id'])

    context['menus_json'] = json.dumps(tree_menus)
    context['topics_json'] = json.dumps(tree_topics)
    return context
