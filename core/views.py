from __future__ import print_function
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClientCreationForm
from .models import Client, PregnancyEvent, Pregnancy
from django.utils import timezone
from calendar_api import create_calendar_entry
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
import json
import datetime

# Create your views here.


def get_index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def create_client(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            client = form.save()

            preg = Pregnancy()
            preg.client = client
            preg.due_date = request.POST.get('due_date', timezone.now())
            preg.week_care_commences = request.POST.get('purchased_plan')
            preg.save()

            # e = {'name': preg.client.name,
            #      }
            # create_calendar_entry(e)

            return redirect(client_details, client.pk)
    else:
        form = ClientCreationForm()

    args = {'form': form}
    return render(request, 'create.html', args)

@login_required(login_url='/login/')
def client_list(request):
    clients = Client.objects.filter()
    return render(request, "client_list.html", {'clients': clients})


def client_details(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, "client_detail.html", {'client': client})


