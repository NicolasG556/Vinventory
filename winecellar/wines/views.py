from django.shortcuts import render


def hello(request):
    return render(request,
                  'wines/hello.html')
