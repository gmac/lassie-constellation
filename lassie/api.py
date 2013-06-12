from tastypie import fields
from tastypie.api import Api
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from tastypie.resources import ModelResource
from lassie.interaction.models import Action, Dialogue
from lassie.inventory.models import Item
from lassie.scene.models import Scene, Layer, Grid, Matrix


# API Resources

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
    
    class Meta:
        queryset = Layer.objects.all()
        resource_name = 'layer'
        always_return_data = True
        authorization = Authorization()
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
        authorization = Authorization()
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
        authorization = Authorization()
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
                

class ActionResource(ModelResource):
    '''
    API resource for accessing action profiles (script and dialogue).
    '''
    content_object = GenericForeignKeyField({
        Item: ItemResource,
        Layer: LayerResource,
    }, 'content_object')
        
    class Meta:
        resource_name = 'action'
        queryset = Action.objects.all()
        always_return_data = True
        authorization = Authorization()
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

    class Meta:
        queryset = Dialogue.objects.all()
        resource_name = 'dialogue'
        always_return_data = True
        authorization = Authorization()
        filtering = {
            'action': ALL_WITH_RELATIONS,
        }


# API structure

v1_api = Api(api_name='v1')

v1_api.register(ItemResource())
v1_api.register(ActionResource())
v1_api.register(DialogueResource())
v1_api.register(SceneResource())
v1_api.register(LayerResource())
v1_api.register(GridResource())
v1_api.register(MatrixResource())

