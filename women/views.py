from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from women.models import Women, Category
from women.serializers import WomenSerializer
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

# Create your views here.


class WomenAPIList(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class WomenAPIDestroy(RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )
