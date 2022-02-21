from django.http import HttpResponse
from django.shortcuts import render
from weather import *


def index(request):
    context = get_current_forecast("40.7128", "-74.0060")
    # context = {}
    context['graph'] = get_weekly_forecast("40.7128", "-74.0060")
    # return HttpResponse(result)
    return render(request, 'index.html', context)
    # return render(request, result)