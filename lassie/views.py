from django.http import HttpResponse

def site_index(request):
    return HttpResponse('online.')
    

def test_page(request):
    return HttpResponse('test')