from django.contrib import admin

from stadium.models import Stadiums, Tickets


@admin.register(Stadiums)
class StadiumsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    pass

