from django.http import HttpResponse


def site_index(request):
    return HttpResponse('online.')