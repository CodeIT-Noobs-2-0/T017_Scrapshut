from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework.response import Response
from account.models import User, Donor, NGO_Admin
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions
from .serializers import *
from .serializers import UserDisplaySerializer, UserSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404



class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserDisplayView(APIView):
    queryset = User.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User.objects.all(), pk=pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data})
        users = User.objects.all()
        serializer = UserDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})

class DonorDisplayView(APIView):
    queryset = Donor.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(Donor.objects.all(), pk=pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data})
        users = User.objects.all()
        serializer = DonorDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})


class NGOAdminDisplayView(APIView):
    queryset = NGO_Admin.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(NGO_Admin.objects.all(), pk=pk)
            serializer = UserSerializer(user)
            return Response({"user": serializer.data})
        users = NGO_Admin.objects.all()
        serializer = NGOAdminDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})


class DonatedDisplayView(APIView):
    queryset = Donated.objects.all()
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(NGO_Admin.objects.all(), pk=pk)
            serializer = DonatedSerializer(user)
            return Response({"user": serializer.data})
        users = NGO_Admin.objects.all()
        serializer = DonatedDisplaySerializer(users, many=True)
        return Response({"users": serializer.data})