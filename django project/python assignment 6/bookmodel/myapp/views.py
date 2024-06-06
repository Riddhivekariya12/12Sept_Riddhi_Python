
from sqlite3 import SQLITE_AUTH_USER
from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getall(request):
    bdata=book.objects.all()
    serial=BookSerializer(bdata,many=True)
    return Response(data=serial.data)


@api_view(['GET'])
def getbookid(request,id):
    try:
        bookid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  

    serial=BookSerializer(bookid)
    return Response(data=serial.data,status=status.HTTP_200_OK)  

@api_view(['DELETE'])
def deletebookid(request,id):
    try:
        bookid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  

    book.delete(bookid)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE','GET'])
def deletebookid(request,id):
    bookid=''
    if request.method=='GET':
      try:
        bookid=book.objects.get(id=id)
      except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
      serial=BookSerializer(bookid)
      return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
       book.delete(bookid)
       return Response(status=status.HTTP_202_ACCEPTED)
    

@api_view(['post'])    
def savebdata(request):
    if request.method=='POST':
       serial=BookSerializer(data=request.data)
       if serial.is_valid():
          serial.save()
          return Response(status=status.HTTP_201_CREATED)
       else:
          return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
       return Response (status=status.HTTP_400_BAD_REQUEST)  



@api_view(['PUT'])
def updatebdata(request,id):
   try:
      bookid=book.objects.get(id=id)
   except   book.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serial=BookSerializer(bookid)
      return Response(data=serial.data,status=status.HTTP_200_OK)   
   if request.method=='PUT':
      serial=BookSerializer(request.data)
      if serial.is_valid():
         serial.save()
         return Response(status=status.HTTP_201_CREATED)
      else:
          return Response(status=status.HTTP_400_BAD_REQUEST)
   else:
       return Response (status=status.HTTP_400_BAD_REQUEST) 
       

     
     

    

    



