from django.core import serializers
from django.shortcuts import render, get_object_or_404
from lassie.scene.models import Scene


def scene_edit(request, scene_id):
	scene = get_object_or_404(Scene, pk=scene_id)
	return render(request, 'scene/scene-edit.html', {
	    'scene': scene,
	    'json': serializers.serialize('json', [scene]),
	})