from django.shortcuts import render

# Create your views here.
def contact_page(request):
    return render(request, 'Contact_page/contact_page.html')