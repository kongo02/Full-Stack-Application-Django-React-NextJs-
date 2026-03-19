from django.contrib import admin
from .models import Ratings


class RatingAdmin(admin.ModelAdmin):
    list_display = ("rater", "agent", "rating")
    

# Register your models here.
admin.site.register(Ratings, RatingAdmin)