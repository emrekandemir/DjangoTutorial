from django.http import JsonResponse
from .models import kategori

def testapi(request):

    key = kategori.objects.filter(pk=1)
    return JsonResponse({'name': str(key[0].title), 'email': 'peter@example.org'})

