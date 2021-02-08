"""post views"""
# django
from django.shortcuts import render
from django.http import HttpResponse

# other
import json
from datetime import datetime

posts = [
    {
        'name': 'mont blanc',
        'user': 'yesica cortez',
        'timestamp': datetime.now().strftime('%Y/%m/%d - %H:%M:%S')
    },
    {
        'name': 'Uzz',
        'user': 'felipe Diaz',
        'timestamp': datetime.now().strftime('%Y/%m/%d - %H:%M:%S')
    }

]
def list_posts(request):
    res = {
        'status': 'A200',
        'message': 'ok',
        'description': [1,2,3,4,5,6,7]
    }
    return HttpResponse(
        json.dumps(res)
    )

def list_postCGI(request):
    """lista de posts como si fuera una CGI app

    Args:
        request (httpRequest): httpRequest

    Returns:
        FormatJson: HttpResponse
    """    
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
        """.format(**post))
    return HttpResponse(
        '<br>'.join(content)
    )