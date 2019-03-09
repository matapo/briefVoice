from django.db import models
from .signal_names import signal_names_list

class SignalData(models.Model):
    time = models.DateTimeField("Time", auto_now_add=True)

for name in signal_names_list:
    SignalData.add_to_class(name, models.DecimalField(max_digits=20,decimal_places=2))
