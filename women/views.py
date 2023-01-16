from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from women.models import Women, Category
from women.serializers import WomenSerializer


# Create your views here.


class WomenViewSet(ReadOnlyModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class WomenAPIList(ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

