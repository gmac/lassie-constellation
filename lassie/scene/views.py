from django.core import serializers
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from lassie.scene.models import Scene, Layer


def scene_index(request):
    return render(request, 'scene/index.html', {})


def scene_edit(request, scene_id):
	scene = get_object_or_404(Scene, pk=scene_id)
	context = {
	    'scene': scene,
	    'json': serializers.serialize('json', [scene]),
	}
	return render(request, 'scene/edit.html', context)
	

def scene_layer(request, layer_id):
    layer = get_object_or_404(Layer, pk=layer_id)
    content_type = ContentType.objects.get_for_model(layer)
    
    return render(request, 'scene/layer.html', {
        'model': layer
    })