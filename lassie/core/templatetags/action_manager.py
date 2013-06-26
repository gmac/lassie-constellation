import json
from django import template
from django.contrib.contenttypes.models import ContentType
from lassie.core.models import Action, ActionType, Intonation, Item, Voice

register = template.Library()

# @register.filter
# def empty_false(value):
#     return ''


@register.inclusion_tag('templatetags/action-manager.html')
def action_manager(model):
    
    # Configuration param constants:
    SINGLE = 'single'
    MULTI = 'multi'
    ITEM_TYPE = 'items'
    ITEM_OPTIONS = 'item options'
    DYNAMIC = 'dynamic'

    # Discrete editor configurations:
    editor_configs = {
        'scene': {MULTI, DYNAMIC, ITEM_TYPE, ITEM_OPTIONS,},
        'item': {MULTI,},
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

    
    # TYPES / VOICES
    # Provide interaction types & voices:
    all_types = ActionType.objects.all()
    all_voices = Voice.objects.all()
    
    # Make sure there's at least one custom action type:
    if (not all_types.filter(is_custom=True).exists()):
        ActionType.objects.create(label='Default Action (Rename!)', is_custom=True)
    
    # Make sure there's at least one voice:
    if (not all_voices.exists()):
        Voice.objects.create(label='Default Voice (Rename!)')
    
    # Remove item type when not applicable:
    if (not ITEM_TYPE in editor_settings):
        all_types = all_types.exclude(is_item=True)
    
    # Create lists and map id references:
    all_types = list(all_types.values('id', 'label'))
    all_voices = list(all_voices.values('id', 'label'))
    
    for actiontype in all_types:
        actiontype['id'] = '/api/v1/actiontype/{0}/'.format(actiontype['id'])
    
    for voice in all_voices:
        voice['id'] = '/api/v1/voice/{0}/'.format(voice['id'])
    
    # Define types and voices:
    context['types_json'] = json.dumps(all_types)
    context['voices_json'] = json.dumps(all_voices)
    
    
    # ITEMS
    # Provide item options, when applicable:
    if (ITEM_OPTIONS in editor_settings):
        all_items = list(Item.objects.values('id', 'slug'))
        
        for item in all_items:
            item['id'] = '/api/v1/item/{0}/'.format(item['id'])
            
        context['items_json'] = json.dumps(all_items)
    

    # ACTIONS
    if (model.actions):
        
        all_actions = model.actions.all().values()
    
        # Forcibly create a new action for singular action records:
        if (not all_actions.exists() and not context['allow_multiple']):
            action_type = ActionType.objects.filter(is_custom=True)[:1].get()
            model.actions.create(action_type=action_type)
            
        context['actions_json'] = json.dumps(list(all_actions))
    
    
    return context
