from django.shortcuts import render
from .serializers import *
from rest_framework import generics,viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters.rest_framework
from .models import *

# Create your views here.
class ParagraphsList(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Paragraphs.objects.all()
    serializer_class = ParagraphsSerializer 
   
class ParagraphsGet(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Paragraphs.objects.all()
    serializer_class = ParagraphsSerializer

class WordSearch(APIView):
    
    def get(self,request,id,word):
        paragraph = Paragraphs.objects.get(id=id)
        paragraphs = paragraph.paragraphs.lower().split('\r\n\r\n')
        datadict = {}
        count = 1
        for para in paragraphs:
            datadict[count]=para
            count+=1
        ids = []
        count = 1
        # print(datadict)
        for key, val in datadict.items():
            if count == 11:
                break
            if word.lower() in val:
                ids.append(key)
                count+=1
        returnData = "Paragraph {} are returned".format(ids)
        # print(returnData)
        return Response(returnData)
        