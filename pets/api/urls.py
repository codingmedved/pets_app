from django.conf.urls import url, include
from ..api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pets', views.PetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]