from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ticket(models.Model):
    ticket_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )

    def __str__(self):
        return f"Ticket for {self.ticket_holder}"
