"""photogram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#django
from django.contrib import admin
from django.urls import path

#custom
from photogram import views as local_views
from posts import views as post_views


websocket = path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hellow_world/',local_views.hello_world),
    path('sorted/',local_views.sorted_numbers),
    path('hi/<str:name>/<int:age>',local_views.say_hi),
    path('posts/',post_views.list_posts),
    path('CGIposts/',post_views.list_postCGI),
    path('renposts/',post_views.list_render)
]
