from tastypie import fields
from tastypie.api import Api
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from tastypie.resources import ModelResource
from lassie.interaction.models import ActionType, Action, Dialogue, Voice
from lassie.inventory.models import Item, ItemCombo
from lassie.player.models import DefaultResponse
from lassie.scene.models import Scene, Layer, Grid, Matrix


# API Resources

class VoiceResource(ModelResource):
    '''
    API resource for accessing voices.
    '''
    class Meta:
        queryset = Voice.objects.all()
        resource_name = 'voice'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }
        
        
class SceneResource(ModelResource):
    '''
    API resource for accessing scene layouts.
    '''
    class Meta:
        queryset = Scene.objects.all()
        resource_name = 'scene'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }      


class LayerResource(ModelResource):
    '''
    API resource for accessing layers within scene layouts.
    '''
    scene = fields.ForeignKey(SceneResource, 'scene')
    voice = fields.ForeignKey(VoiceResource, 'voice', null=True)
    
    class Meta:
        queryset = Layer.objects.all()
        resource_name = 'layer'
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
            'id': ALL,
        }

            
class GridResource(ModelResource):
    '''
    API resource for accessing grids within scene layouts.
    '''
    scene = fields.ForeignKey(SceneResource, 'scene')

    class Meta:
        queryset = Grid.objects.all()
        resource_name = 'grid'
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }

            
class MatrixResource(ModelResource):
    '''
    API resource for accessing matrices within scene layouts.
    '''
    scene = fields.ForeignKey(SceneResource, 'scene')

    class Meta:
        queryset = Matrix.objects.all()
        resource_name = 'matrix'
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }


class ItemResource(ModelResource):
    '''
    API resource for accessing inventory items.
    '''
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }

                
class ItemComboResource(ModelResource):
    '''
    API resource for accessing inventory item combos.
    '''
    class Meta:
        queryset = ItemCombo.objects.all()
        resource_name = 'itemcombo'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }


class DefaultResponseResource(ModelResource):
    class Meta:
        queryset = DefaultResponse.objects.all()
        resource_name = 'defaultresponse'
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'action': ALL_WITH_RELATIONS,
        }


class ActionTypeResource(ModelResource):
    '''
    API resource for accessing action type classifications.
    '''
    class Meta:
        queryset = ActionType.objects.all()
        resource_name = 'action_type'
        allowed_methods = ['get']
                  

class ActionResource(ModelResource):
    '''
    API resource for accessing action profiles (script and dialogue).
    '''
    action_type = fields.ForeignKey(ActionTypeResource, 'action_type', null=True)
    related_item = fields.ForeignKey(ItemResource, 'related_item', null=True)
    content_object = GenericForeignKeyField({
        DefaultResponse: DefaultResponseResource,
        Item: ItemResource,
        ItemCombo: ItemComboResource,
        Layer: LayerResource,
    }, 'content_object')
        
    class Meta:
        resource_name = 'action'
        queryset = Action.objects.all()
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
            'content_object': ALL,
            'content_type': ['exact'],
            'object_id': ['exact'],
        }
                
                
class DialogueResource(ModelResource):
    '''
    API resource for accessing dialogue.
    '''
    action = fields.ForeignKey(ActionResource, 'action')
    voice = fields.ForeignKey(VoiceResource, 'voice')

    class Meta:
        queryset = Dialogue.objects.all()
        resource_name = 'dialogue'
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'action': ALL_WITH_RELATIONS,
            'voice': ALL_WITH_RELATIONS,
        }


# API structure

v1_api = Api(api_name='v1')
v1_api.register(ActionResource())
v1_api.register(ActionTypeResource())
v1_api.register(DefaultResponseResource())
v1_api.register(DialogueResource())
v1_api.register(GridResource())
v1_api.register(ItemComboResource())
v1_api.register(ItemResource())
v1_api.register(LayerResource())
v1_api.register(MatrixResource())
v1_api.register(SceneResource())
v1_api.register(VoiceResource())
