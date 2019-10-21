from .models import *
from django.http import JsonResponse




def homepage(request):

    degisken = ModelAdi.objects.filter(pk=1).first()

    result = {
        'title': degisken.title,
        'link': "",
        'description': "",
    }

    return JsonResponse(result)