from cmath import e
from django.http import HttpResponse, JsonResponse
from .models import *
import random
# Create your views here.\
def home(requests):
    return HttpResponse("hello bitches")


#this is response prototype that we are going to use below
'''{
    'status':True,
    'data':[here we are storing data in a list
        {this is for object}
        ]
}'''


def get_quiz(requests):
    try:
        questionobj=Question.objects.all()
        data=[]

        random.shuffle(list(questionobj)) #this shuffles the object that is created 

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
