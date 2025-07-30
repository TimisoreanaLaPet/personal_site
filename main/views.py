from django.shortcuts import render
from .forms import SubscribeForm

def home(request):
    return render(request, 'home.html')

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'subscribe_success.html', {'name': form.cleaned_data['name']})
    else:
        form = SubscribeForm()
    return render(request, 'subscribe.html', {'form': form})

