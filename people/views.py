from rest_framework import viewsets

from .models import Identity, Person
from .serializers import IdentitySerializer, PersonSerializer

import rest_framework.permissions as permissions

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

    def create(self, request, *args, **kwargs):
        """
        summary of person_create

        descriptive body of person_create
        """
        super(PersonViewSet,self).create(request,args,kwargs)

class IdentityViewSet(viewsets.ModelViewSet):
    model = Identity
    queryset = Identity.objects
    serializer_class = IdentitySerializer
