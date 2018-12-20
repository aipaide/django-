"""mytestproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url

# rest framework
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

#drf schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info=openapi.Info(
    title="MyTesting API",
    default_version='1.0.0',
    description="这是一个测试API",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="jiangweirong10@163.com"),
    license=openapi.License(name="BSD License"),
)
schema_view = get_schema_view(
   swagger_info,
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', include('people.urls')),

    #JSON & YAML view of API(/swagger.json & /swagger.yaml)
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # swagger ui
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # redoc ui
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # cached
    url(r'^cached/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='cschema-json'),
    url(r'^cached/swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='cschema-swagger-ui'),
    url(r'^cached/redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='cschema-redoc'),

    url(r'^internal/doc/', include_docs_urls(title='Your API',
                                    authentication_classes=[],
                                    permission_classes=[])),
]
