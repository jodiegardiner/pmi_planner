from django.shortcuts import render
from .forms import ClientCreationForm
# Create your views here.


def get_index(request):
    return render(request, 'base.html')


def create_client(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClientCreationForm()

    args = {'form': form}
    return render(request, 'create.html', args)
