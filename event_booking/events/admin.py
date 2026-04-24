from django.contrib import admin
from .models import Event, Booking

# Event Admin
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'tickets_available')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description', 'location')
    ordering = ('-date',)
    list_per_page = 10

# Booking Admin
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'tickets_booked', 'booked_at')
    list_filter = ('event', 'booked_at')
    search_fields = ('user__username', 'event__title')
    ordering = ('-booked_at',)
    list_per_page = 10
    
 # Custom header stats
    def changelist_view(self, request, extra_context=None):
        total_bookings = Booking.objects.count()
        extra_context = extra_context or {}
        extra_context['total_bookings'] = total_bookings
        return super().changelist_view(request, extra_context=extra_context)

# Register models with custom admin
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)