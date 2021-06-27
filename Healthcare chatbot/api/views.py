import json
from django.core.serializers import serialize
from functools import wraps
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from base.forms import *
from base.models import *

#this api is for users so we hide other users info
def on_authenticated_user(method,content_type):
    
    def inner_function(view):
        @wraps(view)
        def wrapper(request,*args,**kwargs):
            if request.content_type == content_type:
                if request.method == method:
                    if request.user.is_authenticated:
                        return view(request,*args,**kwargs)
                    else:
                        return HttpResponse("Not authenticated",status=405)
            return HttpResponse("Bad Request",status=400)
        return wrapper
    return inner_function

@on_authenticated_user(method="POST",content_type="application/json")
def post_interview_init(request):
    new_instance = InterviewModel()
    new_instance.user = request.user
    chat = ChatHistory.objects.create()
    new_instance.chat_history = chat
    new_instance.save()
    return JsonResponse({"id":new_instance.pk})
    
@on_authenticated_user(method="POST",content_type="application/json")
def post_interview_setMeta(request,interview_id):
    instance = InterviewModel.objects.get(pk=interview_id)
    body_data = json.loads(request.body.decode("utf-8"))
    body_data = json.loads(body_data)
    print(body_data,type(body_data))
    if instance.user == request.user:
        try:
            new_meta = InterviewMetadataModel(
                age=body_data["age"],
                gender=body_data["gender"],
                is_smoker=body_data["is_smoker"],
                is_pregnant=body_data["is_pregnant"],
                is_obese=body_data["is_obese"],
                is_injured=body_data["is_injured"],
                has_hypertension=body_data["has_hypertension"],
            )
            new_meta.save()
            instance.meta = new_meta
            instance.save()
            return HttpResponse("metadata saved!",status=200)
        except Exception as e:
            print(e)
            return HttpResponse(str(e),status=401)
    else:
        return HttpResponse("Unauthorized",status=401)

@on_authenticated_user(method="POST",content_type="application/json")
def post_interview_addMessage(request,interview_id):
    instance = InterviewModel.objects.get(pk=interview_id)
    body_data = json.load(request.body)
    if instance.user == request.user:
        try:
            new_message = Message(chat=instance.chat_history,**body_data)
            new_message.save()
            return HttpResponse("Message added!",status=200)
        except Exception as e:
            return HttpResponse(str(e),status=401)
    else:
        return HttpResponse("Unauthorized",status=401)

def get_interview(request,interview_id):
    if request.user.is_authenticated:
        instance = InterviewModel.objects.get(pk=interview_id)
        
        if instance.user == request.user:
            sez = {
                "interview_id":instance.pk,
                "creation_date":instance.creation_date,
                "results":instance.results,
                "meta":{
                    "age":instance.meta.age,
                    "gender":instance.meta.gender,
                    "is_smoker":instance.meta.is_smoker,
                    "is_pregnant":instance.meta.is_pregnant,
                    "is_obese":instance.meta.is_obese,
                    "is_injured":instance.meta.is_injured,
                    "has_hypertension":instance.meta.has_hypertension
                    },
                "user_id":instance.user.pk,
                "chat_history":[]
            }
            messages = Message.objects.filter(chat__pk = instance.chat_history.pk)
            for message in messages:
                sez["chat_history"].append({
                    "message":message.message,
                    "date":message.date,
                    "source":message.source
                })
            return JsonResponse(sez)
        else:
            return HttpResponse("Unauthorized",status=401)
    else:
        return HttpResponse("Not authenticated",status=405)

def get_allInterviews(request):
    if request.user.is_authenticated:
        instances = InterviewModel.objects.filter(user__id=request.user.id)
        sez = []
        for instance in instances:
            sez.append({
                "interview_id":instance.pk,
                "creation_date":instance.creation_date,
                "results":instance.results
            })
        return JsonResponse(sez,safe=False)
    else:
        return HttpResponse("Not authenticated",status=405)

def get_disease(request,id):
    if request.user.is_authenticated:
        instance = Disease.objects.get(pk=id)
        sez = {
            "name":instance.name,
            "description":instance.description,
            "cure_method":instance.cure_method,
            "symptoms":[symptom.name for symptom in instance.symptoms.all()],
            "min_age":instance.min_age,
            "max_age":instance.max_age,
            "gender":instance.gender,
            "is_smoker":instance.is_smoker,
            "is_pregnant":instance.is_pregnant,
            "is_obese":instance.is_obese,
            "is_injured":instance.is_injured,
            "has_hypertension":instance.has_hypertension
        }

        return JsonResponse(sez)
    else:
        return HttpResponse("Not authenticated",status=405)
