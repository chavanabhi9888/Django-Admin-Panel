from django.shortcuts import render,redirect
from trainer.form import Enquiry
from trainer.models import trainer
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login')
def add_trainer(request):
    if request.method=='POST':
        f=Enquiry(request.POST)
        
        if f.is_valid():
            f.save()
            return redirect('trainer:trainer')        
    
    formss=Enquiry()

    context = {
        'form':formss
    }  

    return render(request,'index.html',context)

def success_view(request):
    return render(request, 'trainer.html')

@login_required(login_url='dashboard:login') 
def data_list_view(request):
    trainer_list = trainer.objects.all() 
    return render(request, 'trainer_list.html', {'trainer_list': trainer_list})