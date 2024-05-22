from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import task
from .serializers import taskserializer

# Create your views here.

@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        tasks=task.objects.all()
        serializer=taskserializer(tasks,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer=taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE']) 
def task_detail(request,pk):
    try:
        task= task.objects.get(pk=pk)
    except task.doesnotexist:
        return Response(status=status.HTTP_404_NOT_FOUNDt)

    if request.method == 'GET':
        serializer=taskserializer(task)
        return Response(serializer.data)    
    elif request.method == 'PUT':
        serializer=taskserializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
  