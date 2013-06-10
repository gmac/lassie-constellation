import json

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from lassie.scene.models import Scene, SceneObject


def index(request):
    return HttpResponse("Scenes index.")


def get_scene(request, scene_id):
	scene = get_object_or_404(Scene, pk=scene_id)
	return HttpResponse(serializers.serialize('json', [scene]))
	

def get_all_objects(request, scene_id):
    if (request.method == 'POST'):
        objs = serializers.deserialize('json', request.POST['data'])
        objs.save()
        
	objs = SceneObject.objects.get(pk=scene_id)
	return HttpResponse(serializers.serialize('json', [objs]))
		

def get_object(request, scene_id, object_id):
    if (request.method == 'POST'):
        obj = serializers.deserialize('json', request.POST['data'])
        obj.save();
        return HttpResponseRedirect(reverse('scene:scene_object', args=(scene_id, object_id,)))
        
	obj = get_object_or_404(SceneObject, pk=object_id)
	return HttpResponse(serializers.serialize('json', [obj]))

