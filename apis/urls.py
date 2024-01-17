from django import path, include
from rest_framework import routers

from .views import*

router = routers.DefaultRouter()

# define router path and viewset to be used
router.register(r'api', apiViewSet)

urlpattern  = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]