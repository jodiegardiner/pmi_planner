from django.shortcuts import render
from .forms import ClientCreationForm
# Create your views here.


def get_index(request):
    return render(request, 'base.html')


def create_client(request):
    form = ClientCreationForm()
    args = {'form': form}
    return render(request, 'create.html', args)