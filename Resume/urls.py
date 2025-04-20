from django.urls import path
from . import views

urlpatterns = [
    path('api/basicDetails/',views.AddBasicDetails, name='AddBasicDetails'),
    path('api/addExperience/', views.AddExperince, name='AddExperince'),
    path('api/addProjects/', views.AddProject, name='AddProject'),
    path('api/AddSkills/', views.AddSkills, name='AddSkills'),
    path('api/AddEducation/', views.AddSkills, name='AddEducation')
]