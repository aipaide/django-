from rest_framework import viewsets

from .models import Identity, Person
from .serializers import IdentitySerializer, PersonSerializer

import rest_framework.permissions as permissions

class PersonViewSet(viewsets.ModelViewSet):
    model = Person
    queryset = Person.objects
    serializer_class = PersonSerializer
    permission_classes=[permissions.IsAuthenticated,]


class IdentityViewSet(viewsets.ModelViewSet):
    model = Identity
    queryset = Identity.objects
    serializer_class = IdentitySerializer
