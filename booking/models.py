from django.db import models
from django.contrib.auth.models import User
import uuid

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name='Название')
    capacity = models.PositiveSmallIntegerField(verbose_name='Вместимость')
    attendees = models.ForeignKey(User, null=True, related_name='rooms', on_delete=models.SET_NULL,
                                       verbose_name='Ответсвеный')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,  null=True, on_delete=models.SET_NULL, related_name='rooms_author', verbose_name='Создатель')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    def __str__(self):
        return self.name


class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='resources')
    name = models.CharField(max_length=100, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='resource_author', verbose_name='Создатель')

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
        unique_together = (('room', 'name'),)

    def __str__(self):
        return f'{self.name} в {self.room}'


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='booking_rooms')
    resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True, related_name='booking_resourses')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='bookinng')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachments = models.FileField(upload_to='bookings/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Оидание'),
        ('confirmed', 'Согласовано'),
        ('rejected', 'Отклонено')
    ),default=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        unique_together = (('room', 'start_time', 'end_time'),)
        ordering = ('start_time', 'end_time')
        index_together = (('room', 'start_time', 'end_time'),)

    def __str__(self):
        return f'Бронирование {self.room.name} с {self.start_time} по {self.end_time}'