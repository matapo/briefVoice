from django.shortcuts import render
from django.http import HttpResponse

from .models import SignalData

def root_page(request):
    return render(request, "index.html")


def db(request):
    all_signal_data = SignalData.objects.all()
    return render(request, "db.html", {"All signal data": all_signal_data})
