from django.shortcuts import render

def two(request):
    context = ()
    return render(request, 'two.html',{'context': context})
