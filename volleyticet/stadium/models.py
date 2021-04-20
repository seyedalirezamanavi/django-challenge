from django.db import models
from django.contrib.auth.models import User


class Stadiums(models.Model):
    stadium = models.CharField(max_length=100, null=True,)
    total_seats = models.IntegerField(null=True,)
    match_date = models.DateTimeField(null=True,)
    teams = models.CharField(max_length=100, null=True,)
    location = models.CharField(max_length=300, null=True,)

    def __str__(self):
        return f'{self.teams} @ {self.stadium} @ {self.match_date}'



class Tickets(models.Model):
    stadium = models.ForeignKey('Stadiums',
                    on_delete=models.CASCADE,
                    null =True,
    )
    reserved_seats = models.ForeignKey(User,
                    on_delete=models.CASCADE,
                    null =True,
    )
    seat_id = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.reserved_seats} @ {self.stadium}'



