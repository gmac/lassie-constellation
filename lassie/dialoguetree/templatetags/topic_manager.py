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
    tree_topics = TreeTopic.objects.filter(tree=model)
    
    # Create a root menu topic, if none exists.
    if (not tree_menus.count()):
        tree_menus.create(tree=model)
    
    all_menus = list()
    all_topics = list()
    
    for menu in tree_menus:
        all_menus.append({
            'id': menu.id,
            'tree': '/api/v1/tree/{0}/'.format(menu.tree_id),
            'topic': '/api/v1/treetopic/{0}/'.format(menu.topic_id) if menu.topic_id else None,
            'resource_uri': '/api/v1/treemenu/{0}/'.format(menu.id),
        })
    
    for topic in tree_topics:
        all_topics.append({
            'id': topic.id,
            'tree': '/api/v1/tree/{0}/'.format(topic.tree_id),
            'menu': '/api/v1/treemenu/{0}/'.format(topic.menu_id),
            'resource_uri': '/api/v1/treetopic/{0}/'.format(topic.id),
        });

    context['menus_json'] = json.dumps(all_menus)
    context['topics_json'] = json.dumps(all_topics)
    
    return context
