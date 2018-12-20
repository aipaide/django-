from django.conf.urls import url

from .views import IdentityViewSet, PersonViewSet

from rest_framework import routers

# 建立路由器对象。
router = routers.DefaultRouter()

# 注册视图。
router.register('people', PersonViewSet, base_name='people')
