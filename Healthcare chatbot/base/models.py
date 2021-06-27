import uuid,json
from django.db import models
from django.contrib.auth.models import timezone
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
class InterviewMetadataModel(models.Model):
    GENDER = [("M","Male"),("F","Female")]
    age = models.IntegerField(verbose_name="Age",null=True)
    gender = models.CharField(verbose_name="Gender",max_length=1,choices=GENDER,default="M")
    is_smoker = models.BooleanField(verbose_name="Smoker",null=True)
    is_pregnant = models.BooleanField(verbose_name="Pregnant",null=True)
    is_obese = models.BooleanField(verbose_name="Obese",null=True)
    is_injured = models.BooleanField(verbose_name="Injured",null=True)
    has_hypertension = models.BooleanField(verbose_name="Hypertension",null=True)

    def __str__(self):
        return "gender:{},age:{},smoker:{}...".format(self.gender,self.age,self.is_smoker)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.gender=="M" and self.is_pregnant==True):
            return None
        else : return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
class ChatHistory(models.Model):
    #messages (1chat history )  
    def __str__(self):
        try:
            return "Chat For : " + str(self.interview.interview_id)
        except ObjectDoesNotExist:
            return str(self.pk)
        
class Message(models.Model):
    #incomming = from client to chatbot
    #outgoing = from chatbot to client
    SOURCES = [('I','Incomming'),('O','Outgoing')]
    chat = models.ForeignKey(ChatHistory, verbose_name="Chat History", on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=1,choices=SOURCES)
    def __str__(self):
        return self.message

class InterviewModel(models.Model):
    interview_id = models.UUIDField(
        verbose_name="Interview ID",
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    creation_date = models.DateField(
        verbose_name="creation date",
        default=timezone.now
    )
    #holds JSON data for questions,results that the chatbot responded with
    #chat_history
    meta = models.OneToOneField(InterviewMetadataModel,
        verbose_name="Interview Metadata",
        on_delete=models.CASCADE,blank=True,null=True)
    chat_history = models.OneToOneField(ChatHistory, verbose_name="Chat History", on_delete=models.CASCADE,
    related_name="interview")
    results = models.JSONField(default=dict,null=True,blank=True)
    user = models.ForeignKey("user.Patient", verbose_name="patient", on_delete=models.CASCADE)
    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        """Unicode representation of InterviewModel."""
        return str(self.interview_id)

    def get_absolute_url(self):
        """Return absolute url for InterviewModel."""
        return ('')
class Symptom(models.Model):
    name = models.CharField(verbose_name="Symptom name", max_length=60,unique=True)
    #paterns (1Symp to N paterns)
    #responses (1Symp to N responses)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name  
class Disease(models.Model):
    name = models.CharField(verbose_name="Disease name", max_length=60,unique=True)
    description = models.TextField(verbose_name="About the Disease",null=True,blank=True)
    cure_method = models.TextField(verbose_name="Steps to cure the disease",null=True,blank=True)
    symptoms = models.ManyToManyField(Symptom, verbose_name="Symptoms")
    #symtoms (1 Des to N symp)    
    #special condition
    GENDER = [("M","Male"),("F","Female")]
    min_age = models.IntegerField(null=True,blank=True)
    max_age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(verbose_name="Gender",max_length=1,choices=GENDER,blank=True,null=True)
    is_smoker = models.BooleanField(verbose_name="Smoker",null=True)
    is_pregnant = models.BooleanField(verbose_name="Pregnant",null=True)
    is_obese = models.BooleanField(verbose_name="Obese",null=True)
    is_injured = models.BooleanField(verbose_name="Injured",null=True)
    has_hypertension = models.BooleanField(verbose_name="Hypertension",null=True)
    class Meta:
        ordering = ['name']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        valid = True
        if (self.min_age!=None and self.max_age!=None):
            if (self.min_age>self.max_age and self.min_age>=0 and self.max_age>=0):
                valid = False
        if (self.gender!=None and self.is_pregnant!=None):
            if (self.gender=="M" and self.is_pregnant==True):
                valid = False
        if valid:
            return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        else : return None
    @staticmethod
    def compile_disease():
        PATH = "D:\\Daoud\\Progs for fun\\Projex\\Ensias Projects\\Healthcare-chatbot\\Data\\"
        diseases = open(PATH+"diseases.json","w")
        
        Disease_dic = {}
        Disease_queryset = Disease.objects.all()
        index = 0
        for disease in Disease_queryset:
            Disease_dic[index] = {}
            Disease_dic[index]["disease"]=disease.name
            Disease_dic[index]["min_age"]=disease.min_age
            Disease_dic[index]["max_age"]=disease.max_age
            Disease_dic[index]["gender"]=disease.gender
            Disease_dic[index]["is_smoker"]=disease.is_smoker
            Disease_dic[index]["is_pregnant"]=disease.is_pregnant
            Disease_dic[index]["is_obese"]=disease.is_obese
            Disease_dic[index]["is_injured"]=disease.is_injured
            Disease_dic[index]["has_hypertension"]=disease.has_hypertension
            Disease_dic[index]["symptoms"]=[]
            for symptom in disease.symptoms.all():
                Disease_dic[index]["symptoms"].append(symptom.name)
            index +=1
        print(Disease_dic)
        json.dump(Disease_dic, diseases)
        diseases.close()
    @staticmethod
    def compile_intents():
        PATH = "D:\\Daoud\\Progs for fun\\Projex\\Ensias Projects\\Healthcare-chatbot\\Data\\"
        intents = open(PATH+"intents.json","w")
        
        intents_dic = {"intents":[]}
        symptoms_queryset = Symptom.objects.all()
        for symptom in symptoms_queryset:
            intent ={}
            intent["tag"] = symptom.name
            intent["patterns"] = []
            intent["responses"] = []
            for pattern in symptom.paterns.all():
                intent["patterns"].append(pattern.sentence)
            for response in symptom.responses.all():
                intent["responses"].append(response.sentence)
            intents_dic["intents"].append(intent)

        print(intents_dic)
        json.dump(intents_dic, intents)
        intents.close()

    def __str__(self):
        return self.name
class Patern(models.Model):
    symptom = models.ForeignKey(Symptom, verbose_name=("Symptom"), on_delete=models.CASCADE,
    related_name="paterns")
    sentence = models.CharField(verbose_name="Symptom Wording(patern)",max_length=200)
    def __str__(self):
        return "patern id:"+str(self.pk)
class Response(models.Model):
    symptom = models.ForeignKey(Symptom, verbose_name=("Symptom"), on_delete=models.CASCADE,
    related_name="responses")
    sentence = models.CharField(verbose_name="Response patern",max_length=200)
    def __str__(self):
        return "response id:"+str(self.pk)