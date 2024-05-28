import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


def visualization(request):
    return render(request, "visualization.html")
