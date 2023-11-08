from django.shortcuts import render

# Create your views here.
def shopping_cart_page(request):
    return render(request, 'Shopping_cart_page/shoping_cart_page.html')