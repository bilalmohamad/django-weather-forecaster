from django.shortcuts import render
from weather import *

# Retrieves the current forecast and the plot for the weekly forecast and sends the data to the index.html file for data use.
def index(request):
    context = get_current_forecast("40.7128", "-74.0060")
    context['graph'] = get_weekly_forecast("40.7128", "-74.0060")
    return render(request, 'index.html', context)