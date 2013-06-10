from django.core import serializers
from django.shortcuts import render, get_object_or_404
from lassie.scene.models import Scene, SceneObject


def scene_index(request):
    return render(request, 'scene/index.html', {})


def scene_edit(request, scene_id):
	scene = get_object_or_404(Scene, pk=scene_id)
	context = {
	    'scene': scene,
	    'json': serializers.serialize('json', [scene]),
	}
	return render(request, 'scene/edit.html', context)