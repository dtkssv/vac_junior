from django.urls import path


from .views import mainview, vacanciesview, catview, companyview, vacancyview


urlpatterns = [
    path('', mainview, name='main'),
    path('vacancies', vacanciesview, name='vacancies'),
    path('vacancies/cat/<str:category>', catview, name='category'),
    path('companies/<int:company_id>', companyview, name='company'),
    path('vacancies/<int:vacancy_id>', vacancyview, name='vacancy'),

]
