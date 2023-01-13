from django.shortcuts import render
from rest_framework.generics import ListAPIView

from women.models import Women
from women.serializers import WomenSerializer


# Create your views here.


class WomenAPIView(ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
