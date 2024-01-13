from django.shortcuts import render, redirect
from .forms import AppointmentForm

def index(request):
    return render(request, 'index.html')

def app(request):
    success_message = None
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Appointment saved successfully ! An Admin will contact you with the details soon "
    else:
        form = AppointmentForm()

    return render(request, 'appoi.html', {'form': form, 'success_message': success_message})






                  









                