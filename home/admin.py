from django.contrib import admin
from .models import *
admin.site.register(Category)  
class Answer_in(admin.StackedInline):
  model=Answer

class Question_in(admin.ModelAdmin): 
    inlines=[Answer_in]

admin.site.register(Question,Question_in)  
admin.site.register(Answer)  

# Register your models here.
