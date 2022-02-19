from django.urls import path
from .views import TotalMatch

urlpatterns = [
    path('position/<text>/<pk>',TotalMatch.as_view()),
    #path('skill/<pk>',SkillMatch.as_view()),
]