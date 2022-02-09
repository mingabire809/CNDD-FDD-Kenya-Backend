from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('activity/', views.activityListView.as_view()),
    path('activity/<str:pk>/', views.activityDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)