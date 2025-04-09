from django.shortcuts import render

def snow(request):
    context = ()
    return render(request, 'snow.html',{'context': context})


def one(request):
    context = ()
    return render(request, 'one.html',{'context': context})
