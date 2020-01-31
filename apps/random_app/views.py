# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')! for random word")

def generate(request):
    
    if request.session:
        counter = request.session['counter']
        ran_string = get_random_string(length=14)
        context = {
            "ran_string" : ran_string,
            "counter" : counter
        }

        request.session['counter'] += 1

        print(context)

    else:
        request.session['counter'] = 1

    return render(request, "random_app/index.html", context)


def reset(request):
    request.session['counter'] = 1
    counter = request.session['counter']
    context = {
        "counter" : counter
    }
    return render(request, "random_app/index.html", context)