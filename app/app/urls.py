from django.urls import include, path
from rest_framework import routers
from application import views
from django.contrib import admin
from .views import health_check

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin',admin.site.urls),
    path('health/',health_check),
    path('',include('application.urls'))
]