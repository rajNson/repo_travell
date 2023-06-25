from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Next
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Next.objects.all()
    return render(request,'index.html',{'result':obj,'result2':obj2,})

    # return  render(request,'index,html',{'result2':obj2})
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse('HELLO HRU?')