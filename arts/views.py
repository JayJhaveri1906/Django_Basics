from django.shortcuts import render
#to show data we import Arts: - for front end
from .models import Arts

# Create your views here.

def index(request):
    #user page: -
    #in pure python: -
    arts = Arts.objects.all()[:10] 
    # Arts ke andar first 10 objects le and dictionary
    # bana rahe hau and then this dict is passed to first end.: -
    context = {
        #"title":"Latest Arts"
        "arts":arts
    }
    # returning dict to display...: -
    return render(request,"arts/index.html")

