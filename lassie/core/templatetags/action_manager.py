import json
from django import template
from django.contrib.contenttypes.models import ContentType
from lassie.core.models import Action, ActionType, Intonation, Item, Voice

register = template.Library()

# @register.filter
# def empty_false(value):
#     return ''


@register.inclusion_tag('templatetags/action-manager.html')
def action_manager(model, custom_view=False):
    
    # Configuration param constants:
    SINGLE = 'single'
    MULTI = 'multi'
    ITEM_TYPE = 'items'
    ITEM_OPTIONS = 'item options'
    DYNAMIC = 'dynamic'
    CUSTOM_ONLY = 'custom only'

    # Discrete editor configurations:
    editor_configs = {
        'scene': {MULTI, DYNAMIC, ITEM_TYPE, ITEM_OPTIONS, CUSTOM_ONLY,},
        'item': {MULTI, ITEM_TYPE,},
        'itemcombo': {SINGLE,},
        'defaultactionset': {MULTI, ITEM_TYPE,},
        'tree': {SINGLE, DYNAMIC,},
    }
    
    # Define base context:
    content_type = None
    context = {
        'enable_manager': False,
        'error_message': '',
        'content_id': 0,
        'content_type': '',
        'allow_multiple': False,
        'dynamic_install': False,
        'actions_json': '[]',
        'types_json': '[]',
        'items_json': '[]',
        'voices_json': '[]',
        'types': None,
        'items': None,
        'voices': None,
        'tones': Intonation.objects.all(),
    }
    
    # Pull model config settings:
    if (model):
        content_type = ContentType.objects.get_for_model(model)
        context['content_id'] = model.id
        context['content_type'] = content_type.model
        context['enable_manager'] = content_type.model in editor_configs
    
    # Return early if not enabling the manager:
    if (not context['enable_manager']):
        return context
            
    # Proceed with setting up context:
    editor_settings = editor_configs[context['content_type']]
    context['allow_multiple'] = MULTI in editor_settings
    context['dynamic_install'] = DYNAMIC in editor_settings
    
    # Disable custom-only views in basic admin display
    if (CUSTOM_ONLY in editor_settings and not custom_view):
        context['enable_manager'] = False
        return context
        
        
    # TYPES / VOICES
    # Provide interaction types & voices:
    all_types = ActionType.objects.all()
    all_voices = Voice.objects.all()
    
    # Make sure there's at least one custom action type:
    if (not all_types.filter(is_custom=True).exists()):
        ActionType.objects.create(label='Default Action', is_custom=True)
    
    # Make sure there's at least one voice:
    if (not all_voices.exists()):
        Voice.objects.create(label='Default Voice')
    
    # Remove item type when not applicable:
    if (not ITEM_TYPE in editor_settings):
        all_types = all_types.exclude(is_item=True)
    
    # Create lists and map id references:
    all_types = list(all_types.values('id', 'label', 'is_item', 'is_custom'))
    all_voices = list(all_voices.values('id', 'label'))
    
    for actiontype in all_types:
        actiontype['id'] = '/api/v1/actiontype/{0}/'.format(actiontype['id'])
    
    for voice in all_voices:
        voice['id'] = '/api/v1/voice/{0}/'.format(voice['id'])
    
    # Define types and voices:
    context['types'] = all_types
    context['voices'] = all_voices
    context['types_json'] = json.dumps(all_types)
    context['voices_json'] = json.dumps(all_voices)
    
    
    # ITEMS
    # Provide item options, when applicable:
    if (ITEM_OPTIONS in editor_settings):
        all_items = list(Item.objects.values('id', 'slug'))
        
        for item in all_items:
            item['id'] = '/api/v1/item/{0}/'.format(item['id'])
        
        context['items'] = all_items
        context['items_json'] = json.dumps(all_items)
    

    # ACTIONS
    # create new record for singular Actions:
    if (hasattr(model, 'actions') and not context['allow_multiple']):
        all_actions = model.actions.all()

        # Forcibly create a new action for singular action records:
        if (not all_actions.exists()):
            action_type = ActionType.objects.filter(is_custom=True)[:1].get()
            model.actions.create(action_type=action_type)


    return context
