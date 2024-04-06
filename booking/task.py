from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_email(booking_id):
    from booking.models import Booking
    from django.contrib.auth.models import User

    booking = Booking.objects.get(pk=booking_id)
    room = booking.room
    attendees = room.attendees

    subject = 'Новое бронирование'
    message = f'Пришел новый запрос на бронирование {room.name}'
    send_mail(subject, message, None, [attendees.mail])