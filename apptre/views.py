from django.shortcuts import render

def tre(request):
    context = ()
    return render(request, 'tre.html',{'context': context})
