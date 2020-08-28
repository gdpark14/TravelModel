from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile
from main.models import Jasosel
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    regi_form=UserCreationForm()
    profile_form=ProfileForm()
    if request.method=="POST":
        filled_form=UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    return render(request,'signup.html',{'regi_form':regi_form})

def append_revise(request):
    try:
        his_profile=Profile.objects.get(person=request.user)
        if request.user==his_profile.person:
            profile_form=ProfileForm(instance=his_profile)
            if request.method=="POST":
                updated_form=ProfileForm(request.POST,instance=his_profile) 
                if updated_form.is_valid():
                    updated_form.save()
                    return redirect('index')
        return render(request,'profile_revise.html',{'profile_form':profile_form})

    except:
        if request.method=="POST":
            filled_form=ProfileForm(request.POST)
            if filled_form.is_valid():
                temp_form=filled_form.save(commit=False)
                temp_form.person=request.user
                temp_form.save()
                return redirect('index')
        profile_form=ProfileForm()
        return render(request,'profile.html',{'profile_form':profile_form})

def profile_view(request,person_name):
    try:
        compare_obj=User.objects.get(username=person_name)
        person_obj=Profile.objects.get(person=compare_obj)
        his_jss=Jasosel.objects.filter(author=compare_obj)

        return render(request,'profile_view.html',{'person_place':person_obj ,'his_jss':his_jss})
    except:
        return redirect('append_revise')