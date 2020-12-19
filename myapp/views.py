from django.shortcuts import render, redirect

from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News

from .serializers import NewsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class NewsApiView(APIView):

    def get(self, request):
        news_qs = News.objects.all()
        serializer = NewsSerializer(news_qs, many=True)
        return Response(serializer.data)
