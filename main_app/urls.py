from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_user, name='register'),
  path('record/<int:pk>', views.candidate_record, name='record'),
  path('delete_candidate/<int:pk>', views.delete_candidate, name='delete_candidate'),
  path('add_candidate/', views.add_candidate, name='add_candidate'),
  path('update_candidate/<int:pk>', views.update_candidate, name='update_candidate'),
  path('search_candidate/', views.search_candidate, name='search_candidate'),
  path('jobs/', views.job, name='jobs')
  
]

