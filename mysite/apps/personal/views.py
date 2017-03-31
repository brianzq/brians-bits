from django.shortcuts import render


def index(request):
    return render(request, 'personal/index.html')


def contact(request):
    return render(request, 'personal/basic.html', {
        'content': ['If you would like to contact me, please email me',
                    'leapingzhang at gmail dot com']
    })
