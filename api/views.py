from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response

from app.models import CustomUser, Project, Task

from .serilizers import CustomUserSerializers, ProjectSerializers, TaskSerializers
from .permissions import CustomUserPermission, CustomUserDetailPermission, ProjectPermission, ProjectDetailPermission, TaskPermission, TaskDetailPermission

@api_view(['GET', 'POST'])
@permission_classes([CustomUserPermission])
def custom_user(request):
    if request.method == 'GET':
        custom_user = CustomUser.objects.all()
        serializer = CustomUserSerializers(custom_user, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CustomUserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CustomUserDetailPermission])
def custom_user_detail(request, pk):

    customuser = CustomUser.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CustomUserSerializers(customuser)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CustomUserDetailPermission(CustomUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customuser.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@permission_classes([ProjectPermission])
def project(request):
    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectSerializers(project, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ProjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([ProjectDetailPermission])
def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ProjectSerializers(project)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = ProjectDetailPermission(Project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@permission_classes([TaskPermission])
def task(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializers(task, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TaskDetailPermission])
def task_detail(request, pk):

    task = Task.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TaskSerializers(task)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = TaskDetailPermission(Task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)