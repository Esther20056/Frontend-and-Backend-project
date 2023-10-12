from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import peopleSerializer
from rest_framework import serializers
from .models import Post
from .serializer import loginSerializer, peopleSerializer
from rest_framework import status



class articleSerilaizer(serializers.ModelSerializer):
   class Meta :
      model = Post
      fields = "__all__"



# Create your views here.
@api_view(["GET"])
def getALLArticles(request):
   allpost = Post.objects.filter(active = True).all().order_by('-datePosted')

   converted_data = articleSerilaizer(allpost, many=True)
   return Response(converted_data.data)

@api_view(['GET'])
def getArticles(request, id):
   allpost = Post.objects.filter(id = id).first()
   converted_data =  articleSerilaizer(allpost)

   return Response(converted_data.data)

@api_view(['POST'])
def createArticle(request):
   serializer= articleSerilaizer(data=request.data)

   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
   
   else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
      
@api_view(['post'])
def signup(request):
   #  data = request.data['first_name']
   #  print(request.data)
   try:
     new_user = peopleSerializer(data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))

   #  return Response(request.data['username'])
    
# @api_view(['post'])
# def Login(request):
#    # serializer =logSerializer(data=request.data)
#    # if serializer.is_valid():
#    #    serializer.save()
#    #    return Response('Welcome back')
#    # else:
#    #    return Response('Invalid Information')

@api_view(['POST'])
def Login(request):
   try:
   #   print(request.data)
      user = loginSerializer(data=request.data)

      if user.is_valid():
         checkuser = user.loginuser(user.data)
         
         return Response(checkuser, status=status.HTTP_200_OK)
      else:
         return Response(user.errors, status=status.HTTP_400_BAD_REQUEST) 
      
   except BaseException as a :
     return Response(str(a), status=status.HTTP_400_BAD_REQUEST)