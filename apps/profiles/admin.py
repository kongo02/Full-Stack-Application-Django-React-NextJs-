from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pkid","id","user", "phone_number", "gender", "country", "city", "is_buyer", "is_seller", "is_agent", "top_agent", "rating", "num_reviews")
    search_fields = ("user__username", "user__email", "phone_number", "country", "city")
    list_filter = ("gender", "country", "city", "is_buyer", "is_seller", "is_agent", "top_agent")
    list_display_links = ("pkid","id","user")
    ordering = ("-created_at",)

admin.site.register(Profile, ProfileAdmin)
# Register your models here.
