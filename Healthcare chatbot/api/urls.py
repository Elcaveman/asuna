from django.urls import path 
from .views import *

urlpatterns = [
    #*tested in dev
    path('interviews/',get_allInterviews,name="all_interviews"),
    #*
    path('interviews/init/',post_interview_init,name="interview_init"),
    #*
    path('interviews/setMeta/<str:interview_id>/',post_interview_setMeta,name="interview_setMeta"),
    #*
    path('interviews/addMessage/<str:interview_id>/',post_interview_addMessage,name="interview_addMessage"),
    #*
    path('interviews/<str:interview_id>/',get_interview,name="get_interviews"),
    #*
    path('diseases/<int:id>/',get_disease,name="get_disease"),
]