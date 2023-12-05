from django.shortcuts import render

# Existing index view
def index(request):
    return render(request, 'pages/index.html')

# New landing page view
def landing_page(request):
    return render(request, 'pages/landing_page.html')  # Adjust the template path as necessary
