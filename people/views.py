from rest_framework import viewsets
import django_filters.rest_framework as filters
import django_filters
import rest_framework.permissions as permissions
from rest_framework.decorators import permission_classes as permission_decorator
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.inspectors import CoreAPICompatInspector, FieldInspector, NotHandled, SwaggerAutoSchema
from drf_yasg.utils import no_body, swagger_auto_schema

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope,TokenHasResourceScope
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from django.utils.decorators import method_decorator

from .models import Identity, Person
from .serializers import IdentitySerializer, PersonSerializer

class DjangoFilterDescriptionInspector(CoreAPICompatInspector):
    def get_filter_parameters(self, filter_backend):
        if isinstance(filter_backend, filters.DjangoFilterBackend):
            result = super(DjangoFilterDescriptionInspector, self).get_filter_parameters(filter_backend)
            for param in result:
                if not param.get('description', ''):
                    param.description = "Filter the returned list by {field_name}".format(field_name=param.name)

            return result

        return NotHandled

class PersonFilter(django_filters.FilterSet):
    person__first_name=filters.CharFilter(field_name="identity__first_name",lookup_expr="exact")
    person__second_name=filters.CharFilter(field_name="identity__second_name",lookup_expr="exact")
    class Meta:
        model = Person
        fields=["person__first_name","person__second_name"]


class PersonViewSet(viewsets.ModelViewSet):
    """
    PersonViewSet class docstring

    retrieve:
    summary of person_retrieve

    descriptive body of person_retrieve

    """
    model = Person
    queryset = Person.objects
    serializer_class = PersonSerializer
    permission_classes=[permissions.IsAuthenticated,TokenHasResourceScope]
    required_scopes = ['people',]
    authentication_classes = [OAuth2Authentication]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.DjangoFilterBackend,]
    #filter_fields = ('id',)
    filterset_class =PersonFilter



    def create(self, request, *args, **kwargs):
        """
        summary of person_create

        descriptive body of person_create
        """
        return  super(PersonViewSet,self).create(request,args,kwargs)

    @swagger_auto_schema(filter_inspectors=[DjangoFilterDescriptionInspector])
    def list(self, request, *args, **kwargs):
        return super(PersonViewSet,self).list(request,args,kwargs)

    @action(methods=["GET",],detail=False,permission_classes=[permissions.AllowAny,])
    def custom_view(self,request):
        return Response(data={"messgage":"hello world!"})

class IdentityViewSet(viewsets.ModelViewSet):
    model = Identity
    queryset = Identity.objects
    serializer_class = IdentitySerializer


