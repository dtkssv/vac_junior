from django.shortcuts import render
from django.db.models import Count

from .models import Vacancy, Specialty, Company


def mainview(request):
    """Выводит главную страницу"""
    vacancies_by_category = Specialty.objects.annotate(count=Count('vacancies'))
    vacancies_by_company = Company.objects.annotate(count=Count('vacancies'))
    context = {
        'vacancies_by_category': vacancies_by_category,
        'vacancies_by_company': vacancies_by_company,
    }
    return render(request, "index.html", context=context)


def vacanciesview(request):
    """Выводит страницу со всеми вакансиями"""
    vacancies = Vacancy.objects.all()
    count_vacancies = Vacancy.objects.count()

    context = {
        'vacancies': vacancies,
        'count_vacancies': count_vacancies,
    }
    return render(request, 'vacancies.html', context=context)


def catview(request, category):
    """Выводит информацию о выбранной категории вакансий"""
    job_category = Vacancy.objects.filter(speciality__code=category)
    count_job_category = job_category.count()
    category = Specialty.objects.get(code=category)

    context = {
        'job_category': job_category,
        'count_job_category': count_job_category,
        'category': category,
    }
    return render(request, 'category_of_vacancy.html', context=context)


def companyview(request, company_id):
    """Выводит информацию о вакансии выбранной компании"""
    company = Company.objects.get(pk=company_id)
    vacancies_of_company = Vacancy.objects.filter(company__pk=company_id)
    count_vacancies = vacancies_of_company.count()

    context = {
        'company': company,
        'count_vacancies': count_vacancies,
        'vacancies_of_company': vacancies_of_company,

    }
    return render(request, 'company.html', context=context)


def vacancyview(request, vacancy_id):
    """Выводит информацию(описание) вакансии"""
    vacancy = Vacancy.objects.get(pk=vacancy_id)
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'vacancy.html', context=context)
