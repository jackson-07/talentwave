from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_user, name='register'),
  path('candidate/<int:pk>', views.candidate_record, name='candidate'),
  path('delete_candidate/<int:pk>', views.delete_candidate, name='delete_candidate'),
  path('add_candidate/', views.add_candidate, name='add_candidate'),
  path('update_candidate/<int:pk>', views.update_candidate, name='update_candidate'),
  path('search/', views.search, name='search'),
  path('jobs/', views.jobs, name='jobs'),
  path('jobs_detail/<int:pk>', views.jobs_detail, name='jobs_detail'),
  path('jobs_delete/<int:pk>', views.delete_job, name='delete_job'),
  path('add_job/', views.add_job, name='add_job'),
  
]

