from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse



def registration(request):
    RFEO=RegistrationForm()
    d={'RFEO':RFEO}
    if request.method=='POST':
        DRFO=RegistrationForm(request.POST)
        if DRFO.is_valid():
            return HttpResponse(str(DRFO.cleaned_data))

    return render(request,'registration.html',d)
