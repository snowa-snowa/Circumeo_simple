from django.shortcuts import render

def snow(request):
    context = ()
    return render(request, 'snow.html',{'context': context})
