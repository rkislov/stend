from rest_framework import generics
from .models import Room, Resource, Booking
from  .serializers import BookingSerializer


class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def perfom_create(self, serializer):
        serializer.save(created_by=self.request.user)
