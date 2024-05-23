"""
URL configuration for PFM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from appointements.views import index , app 
from Services.views import caterer_list , caterer_details , dj_details, makeup_artist_list , makeup_artist_details , Djs_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('appoi/', include('appointements.urls')),
    path('', index, name='index'),  
    path('app/', app, name='app'),  
    path('Services/', include('Services.urls')),
    path('MakeupArt/',makeup_artist_list ,  name='makeup_artist_list') , 
    path('MakeupDetails/',makeup_artist_details ,  name='makeup_artist_details') ,
    path('Dj/', Djs_list ,  name='Djs_list') , 
    path('DjDetails/',dj_details ,  name='Djs_detail') ,
    path('Traiteur/', caterer_list ,  name='Traiteur_list') , 
    path('Traiteur_list/',caterer_details ,  name='Traiteur_detail') ,

    
    ]





if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

