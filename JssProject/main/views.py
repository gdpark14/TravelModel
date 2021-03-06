from django.shortcuts import render,redirect,get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasosel, Comment,City,Location
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def index(request):
    all_jss=Jasosel.objects.all()
    return render(request,'index.html',{'all_jss':all_jss})

@login_required(login_url='/login/')
def create(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method=="POST":
        filled_form=JssForm(request.POST)
        if filled_form.is_valid():
            temp_form=filled_form.save(commit=False)
            temp_form.author=request.user
            temp_form.save()
            return redirect('index')
    jss_form=JssForm()
    return render(request,'create.html',{'jss_form':jss_form})

def my_index(request):
    my_jss=Jasosel.objects.filter(author=request.user)
    return render(request,'index.html',{'all_jss':my_jss})

@login_required(login_url='/login/')
def detail(request, jss_id):
    # try:
    #     my_jss=Jasosel.objects.get(pk=jss_id)
    # except:
    #     raise Http404
    my_jss=get_object_or_404(Jasosel,pk=jss_id)
    comment_form=CommentForm()

    tourist_location=Location.objects.filter(Q(sigungu__icontains=my_jss.country)&Q(sigungu__icontains=my_jss.city))

    return render(request, 'detail.html',{'my_jss':my_jss,'comment_form':comment_form,'tourist_location':tourist_location})

def delete(request, jss_id):
    my_jss=Jasosel.objects.get(pk=jss_id)
    if request.user==my_jss.author:
        my_jss.delete()
        return redirect('index')
    raise PermissionDenied

def update(request, jss_id):
    
    my_jss=Jasosel.objects.get(pk=jss_id)
    if request.user==my_jss.author:
        jss_form=JssForm(instance=my_jss)
        if request.method=="POST":
            updated_form=JssForm(request.POST,instance=my_jss) 
            if updated_form.is_valid():
                updated_form.save()
                return redirect('index')

    return render(request,'create.html',{'jss_form':jss_form})

def create_comment(request,jss_id):
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form=comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasosel = Jasosel.objects.get(pk=jss_id)
        temp_form.save()

        return redirect('detail',jss_id)

def delete_comment(request, jss_id, comment_id):
    my_comment=Comment.objects.get(pk=comment_id)
    if request.user == my.comment.author:
        my_comment.delete()
        return redirect('detail',jss_id)
    else:
        raise PermissionDenied

def search_index(request):
    Jasosels = Jasosel.objects.all()
    q = request.POST.get('q', "") 
    if q:
        Jasosels = Jasosels.filter(Q(title__icontains=q)|Q(content__icontains=q))
        return render(request, 'index.html', {'all_jss' : Jasosels})
    else:
        return render(request, 'index.html',{'all_jss':Jasosels})

def like(request,jss_id):
    Jasosels = Jasosel.objects.all()
    if request.user.is_authenticated :
        jasosel=get_object_or_404(Jasosel, id=jss_id)
        if request.user in jasosel.like_users.all():
            jasosel.like_users.remove(request.user)
        else:
            jasosel.like_users.add(request.user)
    return render(request,'index.html',{'all_jss':Jasosels})

def location(request,location_name):
    return render(request,'location.html',{'location':location_name})


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})