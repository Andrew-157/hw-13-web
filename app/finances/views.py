from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Income, OutcomeCategory, Outcome
from django.contrib import messages
from django.utils import timezone
from datetime import datetime


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

    income_in_db = Income.objects.filter(
        pub_date=timezone.now().date()).first()
    if income_in_db:
        income_in_db.value += float(income)
        income_in_db.save()

    else:
        new_income = Income(value=float(income))
        new_income.save()

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

    outcome_in_db = Outcome.objects.filter(
        pub_date=timezone.now().date(), category=category).first()

    if outcome_in_db:
        outcome_in_db.value += float(outcome)
        outcome_in_db.save()
    else:
        new_outcome = Outcome(value=float(outcome), category=category)
        new_outcome.save()

    return HttpResponseRedirect(reverse('finances:category', args=(category_name, )))


def statistics(request):
    return render(request, 'finances/statistics.html')


def statistics_income(request):
    return render(request, 'finances/stat_income.html')


def show_income(request):

    if 'start_date' in request.POST:

        income_list = []

        date_1 = request.POST['start_date']
        date_object_1 = datetime.strptime(date_1, r'%Y-%m-%d').date()
        date_2 = request.POST['finish_date']
        date_object_2 = datetime.strptime(date_2, r'%Y-%m-%d').date()

        if date_object_2 > timezone.now().date() or date_object_1 > timezone.now().date():
            message = "You cannot use dates in the future"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_income'))

        if date_object_2 < date_object_1:
            message = "Finish date shouldn't be earlier than the start date"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_income'))

        if date_object_2 == date_object_1:
            message = "Don't enter same dates, you can use another form to choose specific day"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_income'))

        incomes = Income.objects.all()
        for income in incomes:
            if income.pub_date >= date_object_1 and income.pub_date <= date_object_2:
                income_list.append(income.value)

        total_income = sum(income_list)
        print(total_income)
        context = {'date_object_1': date_object_1,
                   'date_object_2': date_object_2, 'total_income': total_income}

        return render(request, 'finances/period_income.html', context)

    if 'specific_date' in request.POST:

        specific_date = request.POST['specific_date']
        date_object = datetime.strptime(specific_date, r'%Y-%m-%d').date()

        if date_object > timezone.now().date():
            message = "You cannot use dates in the future"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_income'))

        object = Income.objects.filter(pub_date=date_object).first()

        if not object:
            income = None
        else:
            income = object.value

        context = {'date_object': date_object, 'income': income}

        return render(request, 'finances/day_income.html', context)


def statistics_outcome(request):
    return render(request, 'finances/stat_outcome.html')


def show_outcome(request):

    outcome_list = []
    categories_list = []
    data_dict = {}

    if 'start_date' in request.POST:

        date_1 = request.POST['start_date']
        date_object_1 = datetime.strptime(date_1, r'%Y-%m-%d').date()
        date_2 = request.POST['finish_date']
        date_object_2 = datetime.strptime(date_2, r'%Y-%m-%d').date()

        if date_object_2 > timezone.now().date() or date_object_1 > timezone.now().date():
            message = "You cannot use dates in the future"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_income'))

        if date_object_2 < date_object_1:
            message = "Finish date shouldn't be earlier than the start date"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_income'))

        if date_object_2 == date_object_1:
            message = "Don't enter same dates, you can use another form to choose specific day"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_outcome'))

        outcomes = Outcome.objects.all()
        for outcome in outcomes:
            if outcome.pub_date >= date_object_1 and outcome.pub_date <= date_object_2:
                outcome_list.append(outcome)

        for outcome in outcome_list:
            categories_list.append(
                OutcomeCategory.objects.filter(name=outcome.category.name).first())

        for category in categories_list:
            sum_for_category = 0
            for outcome in outcomes:
                if outcome.category == category:
                    sum_for_category += outcome.value
                    data_dict[category.name] = sum_for_category

        total_outcome = 0
        for val in data_dict.values():
            total_outcome += val
        context = {'data_dict': data_dict,
                   'date_object_1': date_object_1, 'date_object_2': date_object_2, 'total_outcome': total_outcome}

        return render(request, 'finances/period_outcome.html', context)

    if 'specific_date' in request.POST:

        specific_date = request.POST['specific_date']
        date_object = datetime.strptime(specific_date, r'%Y-%m-%d').date()

        if date_object > timezone.now().date():
            message = "You cannot use dates in the future"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse('finances:stat_outcome'))

        objects = Outcome.objects.filter(pub_date=date_object).all()

        for obj in objects:
            categories_list.append(OutcomeCategory.objects.filter(
                name=obj.category.name).first())

        for category in categories_list:
            sum_for_category = 0
            for obj in objects:
                if obj.category == category:
                    sum_for_category += obj.value
                    data_dict[category.name] = sum_for_category

        total_outcome = 0
        for val in data_dict.values():
            total_outcome += val
        context = {'data_dict': data_dict,
                   'date_object': date_object, 'total_outcome': total_outcome}

        return render(request, 'finances/day_outcome.html', context)
