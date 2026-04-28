from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Incident


# HOME
def home(request):
    return render(request, 'home.html')


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# 🚪 LOGOUT
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


# 🚨 REPORT INCIDENT

def report(request):
    if request.method == 'POST':
        incident_type = request.POST.get('incident_type')
        description = request.POST.get('description')
        latitude = request.POST.get('latitude') or 0
        longitude = request.POST.get('longitude') or 0

        Incident.objects.create(
            user=request.user,
            incident_type=incident_type,
            description=description,
            latitude=float(latitude),
            longitude=float(longitude)
        )

        return redirect('map')

    return render(request, 'report.html')


# 🗺️ MAP PAGE (ROLE-BASED)

def map_view(request):
    if request.user.is_staff:
        incidents = Incident.objects.all().order_by('-created_at')
    else:
        incidents = Incident.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'map.html', {'incidents': incidents})


# 🚨 PANIC BUTTON
@login_required
def panic_incident(request):
    if request.method == "POST":
        try:
            latitude = request.POST.get("latitude") or 0
            longitude = request.POST.get("longitude") or 0

            incident = Incident.objects.create(
                user=request.user,
                incident_type="emergency",  # ⚠️ ensure this exists in your model choices
                description="Emergency triggered via panic button",
                latitude=float(latitude),
                longitude=float(longitude),
                status="Pending"
            )

            return JsonResponse({
                "status": "success",
                "id": incident.id
            })

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)

    return JsonResponse({
        "status": "invalid request"
    }, status=400)


# 📊 USER DASHBOARD (MY REPORTS)
@login_required
def dashboard(request):
    incidents = Incident.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'dashboard.html', {
        'incidents': incidents
    })


# 🚨 DISPATCHER VIEW (ADMIN ONLY)
@login_required
def dispatcher(request):
    if not request.user.is_staff:
        return redirect('home')

    incidents = Incident.objects.all().order_by('-created_at')

    return render(request, 'dispatcher.html', {
        'incidents': incidents
    })