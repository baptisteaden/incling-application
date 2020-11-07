from django.urls import include, path
from rest_framework import routers
from inclingapi.views import TileViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'tiles', TileViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]