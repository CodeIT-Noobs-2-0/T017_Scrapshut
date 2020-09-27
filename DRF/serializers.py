from django.contrib.auth import authenticate
from rest_framework import serializers
from account.models import Donor, NGO_Admin, User
from donation.models import Donated, DonationItem
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField()

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)



class UserDisplaySerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class DonorDisplaySerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Donor.objects.create(**validated_data)

class NGOAdminDisplaySerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return NGO_Admin.objects.create(**validated_data)



class DonatedDisplaySerializer(serializers.Serializer):
'''
    id = serializers.CharField()
    donated_by.first_name = serializers.CharField(max_length=255)
    donated_item.item_name = serializers.CharField(max_length=255)
    donated_quantity = serializers.IntegerField()
    '''
    def create(self, validated_data):
        return Donated.objects.create(**validated_data)

class DonatedSerializer(serializers.Serializer):
    """
    id = serializers.CharField()
    donated_by.first_name = serializers.CharField(max_length=255)
    donated_item.item_name = serializers.CharField(max_length=255)
    donated_quantity = serializers.IntegerField()
"""
    def create(self, validated_data):
        return Donated.objects.create(**validated_data)