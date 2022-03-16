from django.urls import path
from .views import AutoresViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('autores', AutoresViewSet)

urlpatterns = router.urls