from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'David',
        'age': 23,
        'nationality': 'Kenyan'
    }
    return render(request, 'index.html', context) 

def counter(request):
    words = request.POST['words']
    no_of_words = len(words.split())
    return render(request, 'counter.html', {'no_of_words': no_of_words})