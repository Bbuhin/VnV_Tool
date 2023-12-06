from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    # Redirect the root URL
    # path('', RedirectView.as_view(url='/landing-page/', permanent=False)),

    # Existing mainpage view (if still needed elsewhere)
    path('mainpage/', views.mainpage, name='mainpage'),

    # New landing page URL
    path('landing-page/', views.landing_page, name='landing-page'),
]
