from django.http import HttpResponse
# Create your views here.\
def home(requests):
    return HttpResponse("hello bitches")
