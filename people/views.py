from rest_framework import viewsets
import django_filters.rest_framework

from .models import Identity, Person
from .serializers import IdentitySerializer, PersonSerializer

import rest_framework.permissions as permissions
from rest_framework.pagination import LimitOffsetPagination
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
    permission_classes=[permissions.IsAuthenticated,]
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,]
    filter_fields = ('id',)

    def create(self, request, *args, **kwargs):
        """
        summary of person_create

        descriptive body of person_create
        """
        return  super(PersonViewSet,self).create(request,args,kwargs)

    def list(self, request, *args, **kwargs):
        return super(PersonViewSet,self).list(request,args,kwargs)

class IdentityViewSet(viewsets.ModelViewSet):
    model = Identity
    queryset = Identity.objects
    serializer_class = IdentitySerializer
