from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def news(request):
    return render(request, 'main/news.html')