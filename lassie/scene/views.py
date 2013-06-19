from django.core import serializers
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from lassie.scene.models import Scene, Layer


def scene_index(request):
    return render(request, 'scene/index.html', {
        'scenes': Scene.objects.all(),
    })


def scene_edit(request, scene_id):
	scene = get_object_or_404(Scene, pk=scene_id)
	context = {
	    'scene': scene,
	    'json': serializers.serialize('json', [scene]),
	}
	return render(request, 'scene/scene-edit.html', context)