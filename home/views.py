from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#myview
def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')
