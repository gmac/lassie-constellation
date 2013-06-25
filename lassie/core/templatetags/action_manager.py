import json
from django import template
from django.contrib.contenttypes.models import ContentType
from lassie.core.models import ActionType, Intonation, Item, Voice

register = template.Library()

# @register.filter
# def empty_false(value):
#     return ''


@register.inclusion_tag('templatetags/action-manager.html')
def action_manager(model):
    
    # Configuration param constants:
    SINGLE = 'single'
    MULTI = 'multi'
    NO_ITEM_TYPE = 'no item type'
    NO_ITEM_OPTIONS = 'no item options'
    DYNAMIC = 'dynamic'
    
    # Discrete editor configurations:
    editor_configs = {
        'scene': {MULTI, DYNAMIC,},
        'item': {MULTI, NO_ITEM_TYPE, NO_ITEM_OPTIONS,},
        'itemcombo': {SINGLE,},
        'defaultactionset': {MULTI, NO_ITEM_OPTIONS,},
        'tree': {SINGLE, DYNAMIC,},
    }
    
    # Setup context variables:
    content_id = ''
    content_type = ''
    allow_multiple = False
    dynamic_install = False
    all_types = list(ActionType.objects.values())
    all_items = list(Item.objects.values('id', 'slug'))
    all_voices = list(Voice.objects.values('id', 'label'))
    
    if (model):
        content_id = model.id
        content_type = ContentType.objects.get_for_model(model).model
    
    # Test if type is valid:
    valid_type = content_type in editor_configs
    error_message = ''
    
    # Check if content type allows multiple related actions:
    if (valid_type):
        editor_settings = editor_configs[content_type]
        allow_multiple = MULTI in editor_settings
        dynamic_install = DYNAMIC in editor_settings
        
        if (not allow_multiple):
            pass
        
        # Provide no items for default response action selectors:
        if (NO_ITEM_TYPE in editor_settings):
            # TODO: remove "is_item" type from types array...
            pass
             
        # Provide no items for default response action selectors:
        if (NO_ITEM_OPTIONS in editor_settings):
            all_items = list()
                
        if (not all_types or not all_voices):
            error_message = 'Actions editor requires one or more Action Type and Voice options to be defined.'
            valid_type = False
    
    # Format reference ids as API URIs:
    for actiontype in all_types:
        actiontype['id'] = '/api/v1/actiontype/{0}/'.format(actiontype['id'])
        
    for item in all_items:
        item['id'] = '/api/v1/item/{0}/'.format(item['id'])
        
    for voice in all_voices:
        voice['id'] = '/api/v1/voice/{0}/'.format(voice['id'])

    return {
        'valid_type': valid_type,
        'error_message': error_message,
        'content_id': content_id,
        'content_type': content_type,
        'allow_multiple': allow_multiple,
        'dynamic_install': dynamic_install,
        'types_json': json.dumps(all_types),
        'items_json': json.dumps(all_items),
        'voices_json': json.dumps(all_voices),
        'tones': Intonation.objects.all(),
    }
    