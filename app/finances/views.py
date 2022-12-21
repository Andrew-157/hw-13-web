from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Income


def index(request):
    return render(request, 'finances/index.html')


def income(request):
    return render(request, 'finances/income.html')


def outcome(request):
    return HttpResponse("This is outcome page")


def statistics(request):
    return HttpResponse("This is statistics page")


def add_income(request):
    print(request.POST['income'])
    return HttpResponseRedirect(reverse('finances:income'))
