from django.shortcuts import render,redirect
from gym.form import Enquiry
from gym.models import gym
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login')
def addgym(request):
    if request.method=='POST':
        f=Enquiry(request.POST)
        
        if f.is_valid():
            f.save()
            return redirect('gym:success')        
    
    formss=Enquiry()

    context = {
        'form':formss
    }  

    return render(request,'index.html',context)

def success_view(request):
    return render(request, 'success.html')

@login_required(login_url='dashboard:login') 
def data_list_view(request):
    data_list = gym.objects.all() 
    return render(request, 'gym_list.html', {'data_list': data_list})