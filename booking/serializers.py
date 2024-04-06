from rest_framework import serializers
from .models import Room, Resource, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','name','capacity', 'attendees', 'author', 'created_at', 'updated_at')


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        filter = ('id', 'room', 'name', 'author', 'created_at', 'updated_at')


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    resources = ResourceSerializer(many=True)

    class Meta:
        model = Booking
        fields = ('id', 'room', 'resources', 'status', 'created_by', 'created_at', 'updated_at')