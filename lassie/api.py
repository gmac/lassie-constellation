from tastypie import fields
from tastypie.api import Api
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from tastypie.resources import ModelResource
from lassie.core.models import Action, ActionType, DefaultActionSet, Dialogue, Item, ItemCombo, Voice
from lassie.dialoguetree.models import Tree, TreeMenu, TreeTopic
from lassie.scene.models import Scene, Layer, Grid, Matrix


# API Resources

class SceneResource(ModelResource):
    """
    API resource for accessing scene layouts.
    """
    class Meta:
        queryset = Scene.objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }      


class LayerResource(ModelResource):
    """
    API resource for accessing layers within scene layouts.
    """
    scene = fields.ForeignKey(SceneResource, 'scene')
    
    class Meta:
        queryset = Layer.objects.all()
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
            'id': ALL,
        }

            
class GridResource(ModelResource):
    """
    API resource for accessing grids within scene layouts.
    """
    scene = fields.ForeignKey(SceneResource, 'scene')

    class Meta:
        queryset = Grid.objects.all()
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }

            
class MatrixResource(ModelResource):
    """
    API resource for accessing matrices within scene layouts.
    """
    scene = fields.ForeignKey(SceneResource, 'scene')

    class Meta:
        queryset = Matrix.objects.all()
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'scene': ALL_WITH_RELATIONS,
        }


class TreeResource(ModelResource):
    """
    API resource for accessing tree configurations.
    """
    class Meta:
        queryset = Tree.objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }


class TreeMenuResource(ModelResource):
    """
    API resource for accessing tree menu lists.
    """
    tree = fields.ForeignKey(TreeResource, 'tree')
    topic = fields.ForeignKey('lassie.api.TreeTopicResource', 'topic', null=True)
    
    class Meta:
        queryset = TreeMenu.objects.all()
        authorization = DjangoAuthorization()
        always_return_data = True
        filtering = {
            'id': ALL,
            'tree': ALL_WITH_RELATIONS,
            'topic': ALL_WITH_RELATIONS,
        }


class TreeTopicResource(ModelResource):
    """
    API resource for accessing tree topic items.
    """
    tree = fields.ForeignKey(TreeResource, 'tree')
    menu = fields.ForeignKey('lassie.api.TreeMenuResource', 'menu')
    
    class Meta:
        queryset = TreeTopic.objects.all()
        authorization = DjangoAuthorization()
        always_return_data = True
        filtering = {
            'id': ALL,
            'menu': ALL_WITH_RELATIONS,
        }


class ItemResource(ModelResource):
    """
    API resource for accessing inventory items.
    """
    class Meta:
        queryset = Item.objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }

                
class ItemComboResource(ModelResource):
    """
    API resource for accessing inventory item combos.
    """
    class Meta:
        queryset = ItemCombo.objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }


class DefaultActionSetResource(ModelResource):
    class Meta:
        queryset = DefaultActionSet.objects.all()
        always_return_data = True
        authorization = DjangoAuthorization()
        filtering = {
            'action': ALL_WITH_RELATIONS,
        }


class ActionTypeResource(ModelResource):
    """
    API resource for accessing action type classifications.
    """
    class Meta:
        queryset = ActionType.objects.all()
        allowed_methods = ['get']
                  

class ActionResource(ModelResource):
    """
    API resource for accessing action profiles (script and dialogue).
    """
    action_type = fields.ForeignKey(ActionTypeResource, 'action_type', null=True)
    related_item = fields.ForeignKey(ItemResource, 'related_item', null=True)
    content_object = GenericForeignKeyField({
        DefaultActionSet: DefaultActionSetResource,
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


class VoiceResource(ModelResource):
    """
    API resource for accessing voices.
    """
    class Meta:
        queryset = Voice.objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
        }
                
                
class DialogueResource(ModelResource):
    """
    API resource for accessing dialogue.
    """
    action = fields.ForeignKey(ActionResource, 'action')
    voice = fields.ForeignKey(VoiceResource, 'voice')

    class Meta:
        queryset = Dialogue.objects.all()
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
v1_api.register(DefaultActionSetResource())
v1_api.register(DialogueResource())
v1_api.register(GridResource())
v1_api.register(ItemComboResource())
v1_api.register(ItemResource())
v1_api.register(LayerResource())
v1_api.register(MatrixResource())
v1_api.register(SceneResource())
v1_api.register(TreeResource())
v1_api.register(TreeMenuResource())
v1_api.register(TreeTopicResource())
v1_api.register(VoiceResource())
