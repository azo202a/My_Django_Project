from django.urls import path
from . import views
urlpatterns = [
    path('',views. index, name='index'),
    path('home/', views.home, name='home'),  
    path('show/', views.list_students, name='show'),
    path('edit/', views.edit_students, name='edit'),
    path('delete/', views.delete_students, name='delete'),
    path('end/', views.end, name='end'), 
    path('custom-filter/', views.my_view, name='custom_filter'),
    path('students-list/', views.student_table, name='students_list'),
]
