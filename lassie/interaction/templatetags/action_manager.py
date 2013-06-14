import json
from django import template
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from lassie.interaction.models import ActionType, Voice
from lassie.inventory.models import Item

register = template.Library()

@register.filter
def empty_false(value):
    if (value):
        return '1'
    return ''


@register.inclusion_tag('interaction/action-manager.html')
def action_manager(model):
    
    SINGLE = 'single'
    MULTI = 'multi'
    
    allowed_types = {
        'layer': MULTI,
        'item': MULTI,
        'itemcombo': SINGLE,
        'defaultresponse': SINGLE,
    }
    
    content_id = ''
    content_type = ''
    allow_multiple = False
    
    if (model):
        content_id = model.id
        content_type = ContentType.objects.get_for_model(model).model
        
    if (content_type in allowed_types):
        allow_multiple = (allowed_types[content_type] == MULTI)
        
    return {
        'valid_type': content_type in allowed_types,
        'content_id': content_id,
        'content_type': content_type,
        'allow_multiple': allow_multiple,
        'types_json': json.dumps(list(ActionType.objects.values())),
        'items_json': json.dumps(list(Item.objects.values('id', 'slug'))),
        'items': Item.objects.all(),
        'voices': Voice.objects.all(),
    }
    