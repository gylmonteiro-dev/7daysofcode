from django.shortcuts import render
from .requests_test.main import translate_avatars 
# Create your views here.
def list_avatars(request):

    avatars = translate_avatars()
    

    return render(request, 'home.html', context={'avatares': avatars})