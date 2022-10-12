from cmath import e
from django.http import HttpResponse, JsonResponse
from .models import *
import random
# Create your views here.\
def home(requests):
    return HttpResponse("hello bitches")

def get_quiz(request):
    try:
        questionobj=Question.objects.all()
        data=[]
        for values in questionobj:
            data.append({
                "category":values.category.category_name,
                 "question":values.question,
                 "marks":values.marks
            })

        payload={'status':True,'data':data}

        return JsonResponse(payload)

    except Exception as e: 
       print(e)
    return HttpResponse("Something Went Wrong") 
