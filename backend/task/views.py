from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import TodoSerializer
from .models import Todo

class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# # Create your views here.
# @api_view(["GET"])
# def todolist(req):
#     todos = Todo.objects.all()
#     serializer = TodoSerializer(todos,many=True)
#     return Response(serializer.data)
#
# @api_view(["POST"])
# def todocreate(req):
#     serializer = TodoSerializer(data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
#
# @api_view(["DELETE"])
# def tododelete(req,pk):
#     todo = Todo.objects.get(id=pk)
#     todo.delete()
#     return Response("Delete Success")
#
# @api_view(["PUT"])
# def todoupdate(req, pk):
#     todo = Todo.objects.get(id=pk)
#     serializer = TodoSerializer(todo, data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
