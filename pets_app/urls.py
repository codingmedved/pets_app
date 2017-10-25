"""pets_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from users.api.views import login_api_view


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include('pets.api.urls')),
    url(r'^api/v1/schema/$', schema_view),

    url(r'^api/v1/login/$', login_api_view, name='login_api_view'),
]
