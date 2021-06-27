from django.urls import path 
from .views import *

urlpatterns = [
    #*tested
    path('interviews/',get_allInterviews,name="all_interviews"),
    #*tested
    path('interviews/init/',post_interview_init,name="interview_init"),
    #*tested
    path('interviews/setMeta/<str:interview_id>/',post_interview_setMeta,name="interview_setMeta"),
    #!not tested
    path('interviews/addMessage/<str:interview_id>/',post_interview_addMessage,name="interview_addMessage"),
    #*tested
    path('interviews/<str:interview_id>/',get_interview,name="get_interviews"),
    #*tested
    path('diseases/<int:id>/',get_disease,name="get_disease"),
]