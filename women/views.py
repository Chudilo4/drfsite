from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


# Create your views here.


# class WomenAPIView(ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
