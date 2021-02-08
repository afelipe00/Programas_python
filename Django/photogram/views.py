#Django
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
import json

#Utils
from datetime import datetime

def hello_world(request):
    return HttpResponse(
        f'HOLA MUNDO, la hora actual es: {datetime.now().strftime("%d/%m%Y - %H:%M:%S")}'
    )

def sorted_numbers(request):
    #import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET.get('numbers').split(',')]
    numbers = sorted(numbers)
    res = {
        'status': '200',
        'message': 'ok',
        'content': numbers
    }
    return HttpResponse(
        json.dumps(res), content_type='application/json'
    )

def say_hi(request,name,age):
    if age > 15:
        res = {
            'status': 'A200',
            'message': 'ok',
            'description': f'Hola {name} Bienvenido'
        }
    else:
        res = {
            'status': 'A200',
            'message': 'ok',
            'description': f'no se permite el ingreso'
        }
    return HttpResponse(
        json.dumps(res),
        content_type='application/json'
    )