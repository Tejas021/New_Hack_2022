from django.urls import path
from main import views

urlpatterns = [
    # path('',views.IndexView.as_view(),name='index'),
    path('',views.IndexView,name='index'),
    path('problem_list/',views.CompanyProblemsList.as_view(),name='problem_list'),
    path('student_form/',views.StudentFormView.as_view(),name='student_form'),
    
    # Email testing route
    # path('email/', views.email, name='email')
]