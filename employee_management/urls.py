from django.urls import path
from . import views  

#urlpatterns = [
#    path('', views.add_employee, name='home'),  # Redirect root URL to Add Employee page
#    path('add_employee/', views.add_employee, name='add_employee'),
#    path('edit_employee/', views.edit_employee, name='edit_employee'),
#]


urlpatterns = [
    path('', views.add_employee, name='home'),  # Redirect root URL to Add Employee Page
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/', views.edit_employee, name='edit_employee'),
    path('filter/', views.filter_employees, name='filter_employees'),
]
