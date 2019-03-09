from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json

from .models import SignalData

def root_page(request):
    url = '130.82.239.210'
    try:
        serialized_data = urllib2.urlopen(url).read()
        data = json.loads(serialized_data)
    except:
        pass

    return render(request, "index.html")


def db(request):
    all_signal_data = SignalData.objects.all()
    return render(request, "db.html", {"All signal data": all_signal_data})
