from rest_framework import serializers, exceptions
from django_filters.rest_framework import DjangoFilterBackend
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

    def validate(self, data):
        room_id = data.get('room',{}).get('id')
        resource_ids = [resource['id'] for resource in data.get('resources',[])]
        start_time = data.get('strat_time')
        end_time = data.get('end_time')

        overlapping_bookings = Booking.objects.filter(
            models.Q(room__id=room_id) | models.Q(resource__id__in=resource_ids),
            start_time__lte=end_time, end_time__gte=start_time
        ).exclude(id=self.instance.pk if self.instance else None)

        if overlapping_bookings.exists():
            raise exceptions.ValidationError('Уже забронировано')

        return data

    class Meta:
        model = Booking
        fields = ('id', 'room', 'resources', 'status', 'created_by', 'created_at', 'updated_at')