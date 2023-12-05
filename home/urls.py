from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    # Redirect the root URL
    path('', RedirectView.as_view(url='/landing-page/', permanent=False)),

    # Existing index view (if still needed elsewhere)
    path('index/', views.index, name='index'),

    # New landing page URL
    path('landing-page/', views.landing_page, name='landing-page'),
]
