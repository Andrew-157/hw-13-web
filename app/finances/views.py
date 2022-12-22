from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Income
from django.contrib import messages


def index(request):
    return render(request, 'finances/index.html')


def income(request):

    return render(request, 'finances/income.html')


def outcome(request):
    return HttpResponse("This is outcome page")


def statistics(request):
    return HttpResponse("This is statistics page")


def add_income(request):
    income = request.POST['income']
    print(income)
    try:
        float(income)
    except (ValueError, TypeError):
        error_message = "Please, enter numeric values for your incomes"
        messages.add_message(request, messages.INFO, error_message)
        return HttpResponseRedirect(reverse('finances:income'))

    return HttpResponseRedirect(reverse('finances:income'))
