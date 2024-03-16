from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def htmlforms(request):
    if request.method=='POST':
        username=request.POST['un']
        return HttpResponse(username)
    

    return render(request,'htmlforms.html')
