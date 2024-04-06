from django.urls import path
from .views import BookingListView, BookingDetailView, BookingCreateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)