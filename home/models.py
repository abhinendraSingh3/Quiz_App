from unicodedata import category
from django.db import models
import uuid

from django.forms import CharField
from traitlets import default
# Create your models here.

class Base(models.Model):
    uid=models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
 
    class Meta:         #meta is class's skeleton or class's behaviour
        abstract=True   # this means that this class is registered as a base class and we can register/use it anywhere.

class Category(Base):
    category_name=models.CharField(max_length=100) 
    def __str__(self) -> str:
        return self.category_name

class Question(Base):
    #cascade= When the referenced object is deleted, also delete the objects that have references to it.
    #related_name =Its for the reverse relation between question to answers
     category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
     question=models.CharField( max_length=100)
     marks=models.IntegerField(default=5)
     def __str__(self):
         return self.question
     


class Answer(Base): 
    question=models.ForeignKey(Question,related_name='question_name',on_delete=models.CASCADE)
    answer=models.CharField( max_length=100)
    is_correct=models.BooleanField(default=False)
    def __str__(self):
        return self.answer
    


    
