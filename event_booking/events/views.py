import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.db.models import Sum, Count
from django import forms 
from django.core.mail import send_mail 
# --- NAYA IMPORT: User model ko count karne ke liye ---
from django.contrib.auth.models import User 

# -------------------
# Custom Signup Form
# -------------------
class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Valid email address please.")
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

# -------------------
# Signup View
# -------------------
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST) 
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, 'Account created! Now you can login.')
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'events/signup.html', {'form': form})

# -------------------
# Home Page
# -------------------
def home(request):
    if request.user.is_authenticated:
        return redirect('event_list')
    return redirect('signup')

# -------------------
# Event List View
# -------------------
@login_required(login_url='login')
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

# -------------------
# Weather Preview Page
# -------------------
@login_required
def weather_preview(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    weather_data = None
    try:
        api_key = "613ab536d5cfac321f33235657aa2769"
        city = event.location.split(",")[-1].strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response.get("cod") == 200:
            weather_data = {
                'temp': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }
    except Exception as e:
        print(f"Weather API Error: {e}")

    return render(request, 'events/weather_preview.html', {
        'event': event,
        'weather': weather_data
    })

# -------------------
# Book Event View (Weather + Email + Booking)
# -------------------
@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    weather_data = None

    try:
        api_key = "613ab536d5cfac321f33235657aa2769"
        city = event.location.split(",")[-1].strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response.get("cod") == 200:
            weather_data = {'temp': response['main']['temp'], 'description': response['weather'][0]['description'], 'icon': response['weather'][0]['icon']}
    except Exception as e:
        print(f"Weather API Error: {e}")

    if request.method == 'POST':
        tickets_str = request.POST.get('tickets')
        if not tickets_str or not tickets_str.isdigit() or int(tickets_str) < 1:
            messages.error(request, 'Please enter a valid number of tickets.')
            return render(request, 'events/book_event.html', {'event': event, 'weather': weather_data})

        tickets = int(tickets_str)
        if tickets <= event.tickets_available:
            Booking.objects.create(user=request.user, event=event, tickets_booked=tickets)
            event.tickets_available -= tickets
            event.save()

            subject = f'Booking Confirmed: {event.title}'
            message = f'Hi {request.user.username},\n\nYour booking for {event.title} is confirmed!\nTickets: {tickets}\nTotal: ${event.price * tickets}\nLocation: {event.location}'
            try:
                send_mail(subject, message, 'noreply@eventhubpro.com', [request.user.email])
            except:
                pass

            messages.success(request, f'Payment Successful! Confirmation sent to {request.user.email}.')
            return redirect('dashboard')
        else:
            messages.error(request, f'Sorry, only {event.tickets_available} tickets left.')

    return render(request, 'events/book_event.html', {'event': event, 'weather': weather_data})

# -------------------
# Dashboard View (UPDATED WITH USER COUNT)
# -------------------
@login_required
def dashboard(request):
    # 1. Total Bookings (Kitni baar tickets book hui)
    total_reg = Booking.objects.count()
    
    # 2. Total Tickets Sold (Sum of all tickets)
    tickets_query = Booking.objects.aggregate(total=Sum('tickets_booked'))
    total_tickets = tickets_query['total'] if tickets_query['total'] is not None else 0
    
    # 3. Total Events (Available events)
    total_events = Event.objects.count()

    # 4. NAYA FEATURE: Total Members (Kitne users ne signup kiya)
    total_users_count = User.objects.count()

    # 5. Recent Transactions
    recent_users = Booking.objects.select_related('event', 'user').order_by('-booked_at')[:5]

    context = {
        'total_reg': total_reg,
        'total_tickets': total_tickets,
        'recent_users': recent_users,
        'total_events': total_events,
        'total_users_count': total_users_count, # Ye HTML mein use hoga
    }
    return render(request, 'events/dashboard.html', context)

# -------------------
# My Bookings View
# -------------------
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booked_at')
    return render(request, 'events/my_bookings.html', {'bookings': bookings})