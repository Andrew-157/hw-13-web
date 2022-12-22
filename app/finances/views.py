from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Income, OutcomeCategory, Outcome
from django.contrib import messages


def index(request):
    return render(request, 'finances/index.html')


def income(request):
    return render(request, 'finances/income.html')


def add_income(request):
    income = request.POST['income']

    try:

        float(income)

    except (ValueError, TypeError):

        message = "Please, enter numeric values for your incomes"
        messages.add_message(request, messages.INFO, message)

        return HttpResponseRedirect(reverse('finances:income'))

    income = Income(value=float(income))
    income.save()

    return HttpResponseRedirect(reverse('finances:income'))


def outcome(request):
    categories = OutcomeCategory.objects.order_by('id')

    context = {'categories': categories}

    return render(request, 'finances/outcome.html', context)


def add_category(request):
    category = request.POST['category']

    category_in_db = OutcomeCategory.objects.filter(name=category)

    if category_in_db:

        message = f"{category} already exists"
        messages.add_message(request, messages.INFO, message)

        return HttpResponseRedirect(reverse('finances:outcome'))

    new_category = OutcomeCategory(name=category)
    new_category.save()
    return HttpResponseRedirect(reverse('finances:outcome'))


def category(request, category_name):
    category = get_object_or_404(OutcomeCategory, name=category_name)
    context = {'category': category}
    return render(request, 'finances/category.html', context)


def add_outcome(request, category_name, category_id):
    outcome = request.POST['outcome']
    category = OutcomeCategory.objects.filter(pk=category_id).first()
    try:

        float(outcome)

    except (ValueError, TypeError):

        message = "Please, enter numeric values for your outcomes"
        messages.add_message(request, messages.INFO, message)

        return HttpResponseRedirect(reverse('finances:category', args=(category_name,)))

    outcome = Outcome(value=float(outcome), category=category)
    outcome.save()

    return HttpResponseRedirect(reverse('finances:category', args=(category_name, )))


def statistics(request):
    pass
