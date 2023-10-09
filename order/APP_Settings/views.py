from django.shortcuts import render

# Create your views here.
def app_settings(request):
    return render(request, "main/main.html")