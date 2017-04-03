from django.shortcuts import render


def index(request):
    return render(request, 'personal/index.html')


def tags(request):
    return render(request, 'personal/basic.html', {
        'content': ['Coming soon.']
    })
