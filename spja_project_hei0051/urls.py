"""spja_project_hei0051 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from spja_project_hei0051 import settings
import pynstagram.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', pynstagram.views.header, name='header'),
    url(r'^$', pynstagram.views.homepage, name='index'),
    url(r'^users$', pynstagram.views.user_index, name='user_index'),
    url(r'^users/(?P<user_id>\d+)$', pynstagram.views.user, name='user'),
    url(r'^users/(?P<user_id>\d+)/send_email', pynstagram.views.send_email, name='send_email'),
    url(r'^photo/(?P<photo_id>\d+)$', pynstagram.views.photo_index, name='photo_index'),
    url(r'^photo/(?P<photo_id>\d+)/add_comment$', pynstagram.views.add_comment, name='add_comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
