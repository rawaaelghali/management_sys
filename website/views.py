from django.shortcuts import render


# Create views here:
def home(request):
    return render(request, 'home.html', {})
