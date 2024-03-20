from django.urls import path
from .views import Plots_data, HomepageView

urlpatterns = [
    path('home/', HomepageView.as_view(), name='home'),

    # Add more URL patterns as needed

    path('', Plots_data, name='Plots_data'),
]
    # Add more URLs as needed

