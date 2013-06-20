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
    DYNAMIC = 'dynamic'
    
    allowed_types = {
        'layer': {MULTI,},
        'item': {MULTI,},
        'itemcombo': {SINGLE,},
        'defaultresponse': {MULTI,},
        'scene': {MULTI, DYNAMIC,},
    }
    
    content_id = ''
    content_type = ''
    allow_multiple = False
    dynamic_install = False
    all_types = list(ActionType.objects.values())
    all_items = list(Item.objects.values('id', 'slug'))
    all_voices = list(Voice.objects.values('id', 'title'))
    
    if (model):
        content_id = model.id
        content_type = ContentType.objects.get_for_model(model).model
    
    # Check if content type allows multiple related actions:
    if (content_type in allowed_types):
        allow_multiple = MULTI in allowed_types[content_type]
        dynamic_install = DYNAMIC in allowed_types[content_type]
    
    # Provide no items for default response action selectors:
    if (content_type == 'defaultresponse'):
        all_items = list()
        
    return {
        'valid_type': content_type in allowed_types,
        'content_id': content_id,
        'content_type': content_type,
        'allow_multiple': allow_multiple,
        'dynamic_install': dynamic_install,
        'types_json': json.dumps(all_types),
        'items_json': json.dumps(all_items),
        'voices_json': json.dumps(all_voices),
    }
    