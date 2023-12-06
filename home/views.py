from django.shortcuts import render

# Existing index view
def mainpage(request):
    return render(request, 'pages/mainpage.html')

# New landing page view
def landing_page(request):
    return render(request, 'pages/landing_page.html')  # Adjust the template path as necessary
